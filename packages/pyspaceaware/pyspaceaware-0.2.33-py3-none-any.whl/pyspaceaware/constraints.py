import datetime
import numpy as np

from .constants import AstroConstants
from .observer import lla_to_eci
from .time import date_to_jd
from .math import dot, hat, vecnorm
from .coordinates import moon, sun


class ObserverConstraint:
    pass


class SnrConstraint(ObserverConstraint):
    def __init__(self, min_snr: float) -> None:
        self.eval_fcn = lambda **kwargs: _snr(
            **kwargs, snr_limit=min_snr
        )


class ElevationConstraint(ObserverConstraint):
    def __init__(self, min_angle_deg: float) -> None:
        self.eval_fcn = lambda **kwargs: _observer_elevation(
            **kwargs, min_elevation_rad=np.deg2rad(min_angle_deg)
        )


class VisualMagnitudeConstraint(ObserverConstraint):
    def __init__(self, max_visual_magnitude: float) -> None:
        self.eval_fcn = lambda **kwargs: _observer_visual_magnitude(
            **kwargs, maximum_visual_magnitude=max_visual_magnitude
        )


class MoonExclusionConstraint(ObserverConstraint):
    def __init__(self, min_angle_deg: float) -> None:
        self.eval_fcn = lambda **kwargs: _observer_moon_exclusion(
            **kwargs,
            moon_exclusion_angle_min_rad=np.deg2rad(min_angle_deg),
        )


class ObserverEclipseConstraint(ObserverConstraint):
    def __init__(self, station) -> None:
        self.eval_fcn = (
            lambda **kwargs: _observer_eclipsed_geodetic_surface(
                lat_geod=station.lat_geod_rad,
                lon_rad=station.lon_rad,
                **kwargs,
            )
        )


class TargetIlluminatedConstraint(ObserverConstraint):
    def __init__(self) -> None:
        self.eval_fcn = (
            lambda **kwargs: ~_observer_eclipsed_geocentric_eci(
                **kwargs
            )
        )


def _snr(snr: np.ndarray, snr_limit: float, **kwargs) -> np.ndarray:
    return snr > snr_limit


def _observer_eclipsed_geodetic_surface(
    lat_geod: float,
    lon_rad: float,
    dates: np.ndarray[datetime.datetime],
    **kwargs,
) -> np.ndarray:
    """Computes whether a geodetic latitude/longitude is eclipsed at times

    Args:
        lat_geod (float) [rad]: Geodetic latitude of station
        lon_rad (float) [rad]: Longitude of the station
        dates (datetime.datetime nx1) [utc]: Dates to check

    Returns:
        np.ndarray[bool] nx1: Is the station eclipsed at the times?

    """
    station_eci = lla_to_eci(
        lat_geod=lat_geod, lon=lon_rad, a=0, date=dates
    )
    return _observer_eclipsed_geocentric_eci(station_eci, dates)


def _observer_eclipsed_geocentric_eci(
    target_pos_eci: np.ndarray,
    dates: np.ndarray[datetime.datetime],
    **kwargs,
) -> np.ndarray:
    """Computes whether a geocentric position in Earth-Centered Inertial
    coordinates is in eclipse at given dates

    Args:
        target_pos_eci (np.ndarray nx3): Positions to check in ECI
        dates (np.ndarray[datetime.datetime] nx1) [utc]: Dates to propagate to

    Returns:
        float: Volume of the reconstructed convex polytope

    """
    rmag = vecnorm(target_pos_eci)
    sun_eci = sun(date_to_jd(dates))
    ha_arg = np.min(
        np.hstack(
            (AstroConstants.earth_r_eq / rmag, np.ones_like(rmag))
        ),
        axis=1,
        keepdims=True,
    )
    earth_half_angle = np.arcsin(ha_arg)
    sun_half_angle = np.arccos(dot(hat(sun_eci), hat(target_pos_eci)))
    return earth_half_angle > sun_half_angle


def _observer_moon_exclusion(
    look_dir_eci: np.ndarray,
    dates: np.ndarray[datetime.datetime],
    moon_exclusion_angle_min_rad: float,
    **kwargs,
) -> np.ndarray:
    moon_eci = moon(date_to_jd(dates))
    angle_look_to_moon = np.arccos(
        dot(hat(look_dir_eci), hat(moon_eci))
    )
    return angle_look_to_moon > moon_exclusion_angle_min_rad


def _observer_elevation(
    obs_pos_eci: np.ndarray,
    look_dir_eci: np.ndarray,
    min_elevation_rad: float,
    **kwargs,
) -> np.ndarray:
    angle_horizon_to_look = (
        np.arccos(dot(hat(obs_pos_eci), hat(look_dir_eci))) - np.pi / 2
    )
    return angle_horizon_to_look < min_elevation_rad


def _observer_visual_magnitude(
    lc: np.ndarray, maximum_visual_magnitude: float, **kwargs
) -> np.ndarray[bool]:
    lc[lc == 0] = np.nan
    vm = AstroConstants.sun_magnitude - 2.5 * np.log10(
        lc / AstroConstants.sun_irradiance_vacuum
    )
    return vm < maximum_visual_magnitude
