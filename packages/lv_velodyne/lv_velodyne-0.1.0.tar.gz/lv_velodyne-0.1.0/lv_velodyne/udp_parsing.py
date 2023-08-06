import binascii
import socket

from numpy import pi

from lv_velodyne.models import (MODEL_AZIMUTH_OFFSETS, MODEL_ELEVATIONS,
                                MODEL_NAMES)
from lv_velodyne.objects import VelodynePacket

# ----------------------------------------------------------------------------------------------------------------------
# setup

# The data packet comes in the form of 12 data blocks (100 bytes each) followed by a time stamp of
# the first data block (4 bytes), the return type (1 byte), and the model used (1 byte).

# This section contains the overall index structure of the hexidecimal string of the full data
# packet (minus the 42-byte header which is ignored).  Two hexidecimal charicters are equivalent
# to 1-btye of data.  The indexing written out here is in terms of the number of bytes (spelled
# out on p.12 of the programming manual) multiplied by f=2 which converts those indices to the
# indices of the string.

# Channels and blocks
N_CHANNELS = 32
N_BLOCKS = 12

# Byte-to-hex conversion factor
f = 2  # 2 hex characters / byte

# Packet
I_BLOCKS = 0, f * 1200
I_TIME = f * 1200, f * (1200 + 4)
I_RETURN = f * (1200 + 4), f * (1200 + 4 + 1)
I_MODEL = f * (1200 + 4 + 1), f * (1200 + 4 + 1 + 1)

# One block
I_BLOCK = 0, f * 100  # the i^th block: i * f * 100

# In each block
I_FLAG = 0, f * 2
I_AZ = f * 2, f * (2 + 2)
I_CHANNELS = f * (2 + 2), f * (2 + 2 + 3 * N_CHANNELS)

# ----------------------------------------------------------------------------------------------------------------------
# Hexidecimal conversion functions

# These functions are used to take the short hexidecimal string and convert it to the physical
# value that string represents.  This information is documented on pgs.14-15 in the vlp-16
# programmers manual.  These conversions are exactly the same for the vlp-32c.


def hex_to_az(hex):
    """
    Returns the azimuth in degrees given a hexidecimal string.
    """
    # See programming guide (p.13).
    az = hex[2:4] + hex[:2]
    az = int(az, 16) / 100

    return az


def hex_to_dist(hex, model="vlp-16"):
    """
    Returns the distance in units of meters given a hexidecimal string.
    """
    # The vlp-16 has a granularity of 2mm, the vlp-32 of 4mm.
    if model in MODEL_NAMES[16]:
        f = 2
    elif model in MODEL_NAMES[32]:
        f = 4
    else:
        f = 2

    dist = hex[2:4] + hex[:2]
    dist = f * int(dist, 16) / 1e3

    return dist


def hex_to_ref(hex):
    """
    Returns the reflectivity value given a hexidecimal string.
    """
    ref = int(hex, 16)

    return ref


def hex_to_time(hex):
    """
    Returns the time stamp in seconds given a hexidecimal string.
    """
    # See programming guide (p.14).
    time = hex[6:] + hex[4:6] + hex[2:4] + hex[:2]
    time = int(time, 16) * 1e-6

    return time


def hex_to_return(hex):
    """
    Returns the return type string (strongest=37, last=38, dual=39).
    """
    return_type = int(hex)
    if return_type == 37:
        return_type = "strongest"
    elif return_type == 38:
        return_type = "last"
    elif return_type == 39:
        return_type = "dual"
    else:
        print(f"Unrecognized return type value:  '{return_type}'.")

    return return_type


def hex_to_model(hex):
    """
    Returns the model string.
    """
    model_int = int(hex)
    if model_int == 21:
        model_str = "hdl-32e"
    elif model_int == 22:
        model_str = "vlp-16"
    elif model_int == 23:
        model_str = "puck-lite"
    elif model_int == 24:
        model_str = "puck-hi-res"
    elif model_int == 28:
        model_str = "vlp-32c"
    elif model_int == 31:
        model_str = "velarray"
    else:
        raise ValueError(f"Unrecognized device (model) value:  '{model_int}'.")

    return model_str


def get_time_offset(block, channel):
    """
    Returns the time offset between the time stamp (first block, first channel) and the bock and
    channel provided.  This is converted to seconds.
    """
    offset = block * 55.296 + channel * 2.304
    if channel > 16:
        offset += 18.43

    return offset * 1e-6


# ----------------------------------------------------------------------------------------------------------------------


def get_udp_packet(ip, port):
    """
    This uses socket to return the udp message as a hexidecimal string.
    """
    # Use socket to get a udp binary.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(20)
    sock.bind((ip, port))

    # Get data binary if it doesn't time out.
    try:
        udp_bin = sock.recv(65535)
        udp_hex = binascii.hexlify(udp_bin)
        timeout = False

    except socket.timeout as error:
        print("Error: socket timeout")
        print(error)
        udp_hex = None
        timeout = True

    finally:
        sock.close()

    return udp_hex, timeout


def parse_udp_packet(udp_hex):
    """
    Parses the udp hexidecimal string and returns data values.
    """
    # Create the data frame to store data points.  regardless if the vlp is 16 or 32 channel,
    # there will be 32 channels worth of data in a block.
    # N = n_blocks * n_channels

    # Initialize data packet
    packet = VelodynePacket()

    # Get auxilary data
    timestamp = hex_to_time(udp_hex[I_TIME[0] : I_TIME[1]])
    model = hex_to_model(udp_hex[I_MODEL[0] : I_MODEL[1]])
    # return_type = hex_to_return(udp_hex[I_return[0]:I_return[1]])

    # Create a list of blocks and load them with hex data
    blocks_hex = []
    for m in range(N_BLOCKS):
        blocks_hex.append(
            udp_hex[I_BLOCKS[0] : I_BLOCKS[1]][
                I_BLOCK[0] + m * f * 100 : I_BLOCK[1] + m * f * 100
            ]
        )

    # Loop through all data blocks
    for m, block_hex in enumerate(blocks_hex):
        # Grab channel data in hexidecimal form from both firings
        az_hex = block_hex[I_AZ[0] : I_AZ[1]]
        ch_hex = block_hex[I_CHANNELS[0] : I_CHANNELS[1]]

        # Loop through all channels
        for n in range(N_CHANNELS):
            # Set the index:
            # block 1: channels 0-32
            # block 2: channels 32-64
            mn = m * N_CHANNELS + n

            # Get distance and reflectivity hexidecimal data
            dist_hex = ch_hex[f * (n * 3) : f * (n * 3 + 2)]
            ref_hex = ch_hex[f * (n * 3 + 2) : f * (n * 3 + 2 + 1)]

            # Record values into packet
            packet.channels[mn] = n
            packet.reflectivities[mn] = hex_to_ref(ref_hex)
            packet.times[mn] = timestamp + get_time_offset(m, n)

            # Create an array representing the points in spherical coords
            packet.points[mn][0] = hex_to_dist(dist_hex)
            azimuth = hex_to_az(az_hex)

            # Apply azimuth correction for vlp-32c
            if model in MODEL_NAMES[32]:
                azimuth += MODEL_AZIMUTH_OFFSETS[model][n]

            packet.points[mn][1] = azimuth * pi / 180.0
            packet.points[mn][2] = MODEL_ELEVATIONS[model][n] * pi / 180.0

    # Interpolate the second round of firings.  The last block must be extrapolated.  It should be
    # noted here that the actual interpolation should involve each channel independently since
    # they all fire at different times.  The error is of order ~0.5 cm at 100 m and 300 rpm.

    # Interpolate for the first blocks
    for m in range(N_BLOCKS - 1):
        for n in range(16, N_CHANNELS):
            mn = m * N_CHANNELS + n
            this_az = packet.points[mn][1]
            next_az = packet.points[mn + N_CHANNELS][1]
            if next_az < this_az:
                next_az += 2 * pi
            packet.points[mn][1] = (next_az + this_az) / 2

    # Extrapolate for the last block
    for n in range(16, N_CHANNELS):
        mn = (N_BLOCKS - 1) * N_CHANNELS + n
        this_az = packet.points[mn][1]
        last_az = packet.points[mn - N_CHANNELS][1]
        if this_az < last_az:
            this_az += 2 * pi
        packet.points[mn][1] += this_az - last_az

    # Make sure all azimuth values are between 0 and 360
    packet.points[:][1] %= 2 * pi

    return packet
