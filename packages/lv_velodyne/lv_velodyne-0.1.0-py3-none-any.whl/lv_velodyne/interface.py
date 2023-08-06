from json import loads
from math import pi, sqrt
from time import time
from typing import Tuple

from numpy import inf, max, min, where
from requests import exceptions, get, post

from lv_velodyne.objects import VelodynePacket, VelodynePointCloud
from lv_velodyne.udp_parsing import get_udp_packet, parse_udp_packet


class VLPInterface:
    """
    This class manages communications, configurations, meta data, and output data
    to and from the Velodyne LiDAR unit.
    """

    def __init__(
        self,
        ip="192.168.1.201",
        host_ip="192.168.1.77",
        null_ip="255.255.255.255",
        port=2368,
    ):
        self.ip = ip
        self.host_ip = host_ip
        self.null_ip = null_ip
        self.port = port
        self.laser = False

        self.set_host_ip(self.host_ip)

    # GENERAL CONFIGURATIONS

    def save_configs(self):
        """
        Save all configs on the device.
        """
        _ = post(f"http://{self.ip}/cgi/save", {})

    def reset_configs(self):
        """
        Reset all configs via http command.
        """
        _ = post(f"http://{self.ip}/cgi/reset", {})

    # SET METHODS

    def set_host_ip(self, ip):
        """
        Set the device host ip address.
        """
        try:
            resp = post(f"http://{self.ip}/cgi/setting/host", data={"addr": ip})
            resp.raise_for_status()
            self.host_ip = ip
        except exceptions.HTTPError as err_http:
            print("Http Error:", err_http)
        except exceptions.ConnectionError as err_con:
            print("Error Connecting:", err_con)
        except exceptions.Timeout as err_timeout:
            print("Timeout Error:", err_timeout)
        except exceptions.RequestException as err_request:
            print("Request Exception:", err_request)

    def set_return_type(self, return_type):
        """
        Set the return type of the device (strongest, last, dual).
        """
        _ = post(f"http://{self.ip}/cgi/setting", data={"returns": return_type})

    def set_motor_speed(self, rpm):
        """
        Set the motor speed in units of rotations per minute.
        """
        _ = post(f"http://{self.ip}/cgi/setting", data={"rpm": rpm})

    def set_azimuth(self, start, end):
        """
        Set the azimuthal angle between two values.
        """
        if start < 0:
            start = 360 + start

        if end < 0:
            end = 360 + end

        if end < start:
            start, end = end, start

        _ = post(f"http://{self.ip}/cgi/setting/fov", data={"start": start, "end": end})

    def set_laser(self, state=False):
        """
        Toggle the device on and off, or set to a specific state.
        """
        if state in [True, 1, "on"]:
            _ = post(f"http://{self.ip}/cgi/setting", data={"laser": "on"})
            self.laser = True
        elif state in [False, 0, "off"]:
            _ = post(f"http://{self.ip}/cgi/setting", data={"laser": "off"})
            self.laser = False
        else:
            print("invalid argument:  `set_laser(state=False)`")

    # GET METHODS

    def get_configs(self):
        """
        Get all device configurations from the settings json.
        """
        resp = get(f"http://{self.ip}/cgi/settings.json")

        return loads(resp.text)

    def get_status(self):
        """
        Get all device configurations from the settings json.
        """
        resp = get(f"http://{self.ip}/cgi/status.json")

        return loads(resp.text)

    def get_mac(self):
        """
        Get the mac address of the device.
        """
        resp = get(f"http://{self.ip}/cgi/info.json")

        return loads(resp.text)

    def get_snapshot(self):
        """
        Get a snapshot of the device settings.
        """
        resp = get(f"http://{self.ip}/cgi/snapshot.hdl")

        return loads(resp.text)

    def get_diagnostics(self):
        """
        Get useful diagnostic information from the device.
        """
        resp = get(f"http://{self.ip}/cgi/diag.json")

        return loads(resp.text)

    def get_temperature(self):
        """
        Get the temperature of the device in degrees celcius.  The conversion of this can be found
        on page 80 of the vlp-16 user's manual.
        """
        diagnostics = self.get_diagnostics()
        temp_unit = float(diagnostics["volt_temp"]["bot"]["lm20_temp"])

        return -1481.96 + sqrt(2.1962e6 + (1.8639 - (5 * temp_unit / 4096)) / 3.88e-6)

    # POINT CLOUDS

    def snap_pc(
        self,
        r_lim: Tuple[float] = (0.0, 200.0),
        az_lim: Tuple[float] = (0.0, 360.0),
        el_lim: Tuple[float] = (-60.0, 60.0),
    ) -> VelodynePointCloud:
        """
        Returns a single lidar packet (384 points).
        """
        # Order limits and convert angles to radians
        r_lim = (min(r_lim), max(r_lim))
        az_lim = (min(az_lim) * pi / 180.0, max(az_lim) * pi / 180.0)
        el_lim = (min(el_lim) * pi / 180.0, max(el_lim) * pi / 180.0)

        # Get udp packet
        udp_packet, udp_timeout = get_udp_packet(self.host_ip, self.port)
        if udp_timeout is False:
            packet = parse_udp_packet(udp_packet)
        else:
            packet = VelodynePacket()

        # Create the point cloud object
        point_cloud = VelodynePointCloud.from_packet(packet)

        # Limit the point cloud
        point_cloud_subset = point_cloud[
            where(
                (r_lim[0] < point_cloud.points[:, 0])
                & (point_cloud.points[:, 0] < r_lim[1])
                & (az_lim[0] < point_cloud.points[:, 1])
                & (point_cloud.points[:, 1] < az_lim[1])
                & (el_lim[0] < point_cloud.points[:, 2])
                & (point_cloud.points[:, 2] < el_lim[1])
            )[0]
        ]

        return point_cloud_subset

    def record_pc(
        self,
        n_packets: float = inf,
        n_points: float = inf,
        duration: float = 30.0,
        r_lim: Tuple[float] = (0.0, 200.0),
        az_lim: Tuple[float] = (0.0, 360.0),
        el_lim: Tuple[float] = (-60.0, 60.0),
    ) -> VelodynePointCloud:
        """
        Returns an point cloud object from an extended recording.
        """
        # Initialize point cloud object
        point_cloud = VelodynePointCloud()

        # Begin counters
        packet_count = 0
        start = time()

        # Collect data packets
        while time() - start < duration:
            # Parse the udp packet into a smaller point cloud object
            point_cloud.join(self.snap_pc(r_lim=r_lim, az_lim=az_lim, el_lim=el_lim))

            # Update packet count
            packet_count += 1

            # Break if limits are reached
            if packet_count >= n_packets:
                break

            if len(point_cloud) >= n_points:
                break

        return point_cloud


if __name__ == "__main__":
    from lv_physics.core.vectors import Z_AXIS, cross, dot

    print("Connecting")

    # Instantiate and connect to a Velodyne lidar with specific IP and host IP addresses
    lidar = VLPInterface(ip="192.168.1.201", host_ip="192.168.1.77", port=2368)

    print("Adjusting motor speed, setting laser on, and cropping the azimuth range")

    # Set motor speed to 300rpm
    lidar.set_motor_speed(300)

    # Turn the laser on
    lidar.set_laser(True)

    # Set azimuth range to cover 45 degrees left and 45 degrees right
    lidar.set_azimuth(-45, 45)

    # Record a point cloud with 1000 points
    print("Scanning for ~1000 points:", end=" ", flush=True)
    point_cloud_1000_points = lidar.record_pc(n_points=1000)
    print(f"{len(point_cloud_1000_points)} points")
    del point_cloud_1000_points

    # Record a point cloud with 50 packets
    print("Scanning for 50 packets:", end=" ", flush=True)
    point_cloud_50_packets = lidar.record_pc(n_packets=50)
    print(f"{len(point_cloud_50_packets)} points")
    del point_cloud_50_packets

    # Record a 10-second point cloud
    print("Scanning for 5 seconds:", end=" ", flush=True)
    point_cloud = lidar.record_pc(duration=5)
    print(f"{len(point_cloud)} points")

    # Turn the laser off
    lidar.set_laser(False)

    # Process the point clouds (e.g., visualize, analyze, save, etc.)

    # Rotate the point cloud by 180 deg about the z-axis
    point_cloud.rotate(pi, axis=Z_AXIS)

    # The points are stored in a `numpy.ndarray`, with dimension (n_points, 3), so that each element is itself
    # a vector.  This makes it subject to all of the vector operations in the `lv_physics` package.
    point_a = point_cloud.points[7]
    point_b = point_cloud.points[8]
    point_c = point_b - point_a
    point_d = cross(point_b, point_c)
    dot_ab = dot(point_a, point_b)

    # The point cloud returns the points in cartesian and spherical coordinates
    X = point_cloud.points[:, 0]  # [m]
    y = point_cloud.points[:, 1]  # [m]
    Z = point_cloud.points[:, 2]  # [m]

    R = point_cloud.points_sph[:, 0]  # [m]
    AZ = point_cloud.points_sph[:, 1]  # [rad]
    EL = point_cloud.points_sph[:, 2]  # [rad]
