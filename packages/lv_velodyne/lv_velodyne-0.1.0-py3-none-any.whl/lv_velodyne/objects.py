from __future__ import annotations  # Required for type-hinting `PointCloud`

from dataclasses import dataclass, field
from time import time

from dataclasses_json import dataclass_json
from lv_physics.core.dataclass_helpers import array_field
from lv_physics.core.vectors import (cartesian_transform, rotate,
                                     spherical_transform)
from numpy import array, concatenate, float_, int_, zeros
from numpy.typing import NDArray


@dataclass_json
@dataclass
class VelodynePacket:
    """
    Represents a single data packet from a Velodyne Puck (16/32 channel).  The points
    are stored in spherical coordinates [m, rad, rad].  This object is defined to be
    384 points long.
    """

    channels: NDArray[float_] = array_field(default_factory=lambda: zeros(384, float_))
    points: NDArray[float_] = array_field(
        default_factory=lambda: zeros((384, 3), float_)
    )
    reflectivities: NDArray[float_] = array_field(
        default_factory=lambda: zeros(384, int_)
    )
    times: NDArray[float_] = array_field(default_factory=lambda: zeros(384, float_))
    timestamp: float = field(default_factory=time)

    def __len__(self):
        return len(self.times)


@dataclass_json
@dataclass
class VelodynePointCloud:
    """
    Represents a point cloud object with some number of points.  The points here are
    stored in a Cartesian coordinate system.
    """

    channels: NDArray[float_] = array_field(default_factory=lambda: zeros(0, float_))
    points: NDArray[float_] = array_field(default_factory=lambda: zeros((0, 3), float_))
    reflectivities: NDArray[float_] = array_field(
        default_factory=lambda: zeros(0, int_)
    )
    times: NDArray[float_] = array_field(default_factory=lambda: zeros(0, float_))
    timestamp: float = field(default_factory=time)

    @classmethod
    def from_packet(cls, packet: VelodynePacket) -> VelodynePointCloud:
        """Instantiates the object from a `VelodynePacket`"""
        return cls(
            channels=packet.channels.copy(),
            points=cartesian_transform(packet.points),
            reflectivities=packet.reflectivities.copy(),
            times=packet.times.copy(),
            timestamp=packet.timestamp,
        )

    def __len__(self) -> int:
        """Returns the length of the point cloud."""
        return len(self.times)

    def __getitem__(self, item) -> VelodynePointCloud:
        """Returns a sub-selection of a point cloud."""
        return VelodynePointCloud(
            channels=self.channels[item].copy(),
            points=self.points[item].copy(),
            reflectivities=self.reflectivities[item].copy(),
            times=self.times[item].copy(),
            timestamp=self.timestamp + 0.0,
        )

    def join(self, point_cloud: VelodynePointCloud) -> None:
        """Joins another point cloud object to the end of this."""
        self.channels = concatenate([self.channels, point_cloud.channels])
        self.points = concatenate([self.points, point_cloud.points])
        self.reflectivities = concatenate(
            [self.reflectivities, point_cloud.reflectivities]
        )
        self.times = concatenate([self.times, point_cloud.times])

    @property
    def points_sph(self) -> NDArray[float_]:
        """Returns a numpy array of the points in spherical coordinates [m, rad, rad]."""
        return spherical_transform(self.points + 0.0)

    def rotate(
        self,
        angle: float,
        axis: NDArray[float_] = array([0.0, 0.0, 1.0]),
        point: NDArray[float_] = array([0.0, 0.0, 0.0]),
    ):
        """Rotates the point cloud about the point and axis by an angle [rad]."""
        self.points[:] = rotate(
            self.points[:],
            angle=angle,
            axis=axis,
            point=point,
        )
