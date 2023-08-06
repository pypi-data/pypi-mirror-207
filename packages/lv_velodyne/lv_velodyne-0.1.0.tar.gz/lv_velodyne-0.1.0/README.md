# LV-Velodyne

LV-Velodyne is a Python package for working with Velodyne LiDAR data. It provides functionality for parsing, processing,
and analyzing Velodyne point cloud data.

## Prerequisites

- Python 3.7 or higher
- Git (optional, for cloning the repository)
- AWS CLI (for using AWS CodeArtifact)

## Installation

### For Users

#### Setting up AWS

1. Install the AWS CLI by following the
   [official installation guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

2. Configure the AWS CLI with your AWS credentials by running:

   ```
   aws configure
   ```

   Enter your AWS Access Key ID, AWS Secret Access Key, Default region name, and Default output format as prompted.

#### Installing using AWS CodeArtifact

1. Log in to AWS CodeArtifact by running:

   ```
   aws-login "aws codeartifact login --tool pip --domain linevision-dev --repository dev-linevision-pip"
   ```

   Note that you must log in every 24 hours to maintain access to the repository.

2. Install the LV-Velodyne package using pip:

   ```
   pip install lv-velodyne
   ```

#### Alternative: Clone the repository and install using Flit

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/lv-velodyne.git
   cd lv-velodyne
   ```

2. Set up the environment and install the package:

   ```
   make build-env
   make install
   ```

### For Developers

#### Publishing with Flit and bumping the version

1. Ensure that you have valid credentials for the package repository you intend to publish to.

2. Use the Makefile to bump the version, publish the package, and perform other tasks:

   - To bump the major version:

     ```
     make bump-major
     ```

   - To bump the minor version:

     ```
     make bump-minor
     ```

   - To bump the patch version:

     ```
     make bump-patch
     ```

   - To publish the package:

     ```
     make publish
     ```

#### Using the Makefile

The Makefile contains several useful commands for working with the LV-Velodyne package:

- `make build-env`: Set up the Python virtual environment and install the necessary tools.

- `make install`: Install the package and its dependencies.

- `make test`: Run tests for the package.

- `make clean`: Clean up the environment, removing build artifacts and other temporary files.

- `make reset`: Reset the environment, performing a clean and then setting up the environment and installing the
package.

For more information on the available commands, refer to the comments in the Makefile.

## Usage

The central feature of the LV-Velodyne package is the LiDAR interface object, `VLPInterface`.  This object handles the
connection the VLP LiDARs (VLP-16 and VLP-32c), sending configurations to the LiDAR, and extracting point cloud scans
from it.  Here is an example of how to extract the point cloud from the interface connection.
```
from lv_physics.core.vectors import Z_AXIS, cross, dot

from lv_velodyne import VLPInterface
from lv_velodyne.objects import VelodynePointCloud


def main():

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

if __name__ == "__main__":
    main()
```

## Windows Usage

This section is intended for Windows users who want to work with the provided `build.bat` script. The script provides
a convenient way to run various development tasks, such as setting up the environment, installing dependencies, running
tests, and more.

### Prerequisites

Ensure that you have Python installed on your system. You can download and install the latest version of Python from the
official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Using the build.bat script

1. Open the Command Prompt by pressing `Win + R` to open the Run dialog, typing `cmd`, and pressing Enter.

2. Navigate to your project directory using the `cd` command. For example:

   ```
   cd C:\path\to\your\project
   ```

3. To view the available commands, run the script without any arguments:

   ```
   build.bat
   ```

   This will display a list of available commands and a short description for each.

4. To execute a command, run the script with the desired command as an argument. For example, to set up the environment,
   run:

   ```
   build.bat build-env
   ```

   This command will create a new Python virtual environment and install the necessary tools.

5. You can now run other commands as needed. Some examples are:

   - Install production and development dependencies:

     ```
     build.bat install
     ```

   - Run tests:

     ```
     build.bat test
     ```

   - Lint and format your code:

     ```
     build.bat lint
     ```

   - Clean the project directory:

     ```
     build.bat clean
     ```
