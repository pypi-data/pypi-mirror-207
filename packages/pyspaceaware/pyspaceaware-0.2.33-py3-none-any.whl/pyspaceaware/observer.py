import numpy as np
import datetime

from .constants import AstroConstants
from .math import sph_to_cart, stack_mat_mult, hat, dot
from .coordinates import ecef_to_eci


def geodetic_lat_to_geocentric(lat_geod: np.ndarray) -> np.ndarray:
    """Converts geodetic latitude to geocentric latitude

    :param lat_geod: Geodetic latitudes [rad]
    :type lat_geod: np.ndarray
    :return: Geocentric latitudes [rad]
    :rtype: np.ndarray
    """
    f = AstroConstants.earth_f
    return np.arctan((1 - f) ** 2 * np.tan(lat_geod))


def radius_at_geodetic_lat(lat_geodetic: np.ndarray) -> np.ndarray:
    """Earth's radius at the given geodetic latitude

    :param lat_geodetic: Geodetic latitudes [rad]
    :type lat_geodetic: np.ndarray
    :return: Earth radius at given latitudes [km]
    :rtype: np.ndarray
    """
    lat_geoc = geodetic_lat_to_geocentric(lat_geodetic)
    return AstroConstants.earth_r_eq - 21.38 * np.sin(lat_geoc) ** 2


def lla_to_itrf(
    lat_geod: np.ndarray, lon: np.ndarray, a: np.ndarray
) -> np.array:
    """Converts from latitude, longitude, altitude (LLA) to the International Terrestrial Reference Frame (ITRF)

    :param lat_geod: Geodetic latitudes [rad]
    :type lat_geod: np.ndarray [nx1]
    :param lon: Longitudes [rad]
    :type lon: np.ndarray [nx1]
    :param a: Altitudes above the WGS84 ellipsoid [km]
    :type a: np.ndarray [nx1]
    :return: ITRF positions for each LLA triplet [km]
    :rtype: np.array [nx3]
    """
    nrow = lat_geod.size if hasattr(lat_geod, "size") else 1
    lat_geoc = geodetic_lat_to_geocentric(lat_geod)
    # Transforms geodetic latitude into geocentric

    r_earth_at_lat = radius_at_geodetic_lat(lat_geod)
    # Computes the radius of the earth at the given geodetic latitude
    r_topo = r_earth_at_lat + a
    # Computes the altitude of the observer at this point [km]

    (x_itrf, y_itrf, z_itrf) = sph_to_cart(lon, lat_geoc, r_topo)
    return np.array((x_itrf, y_itrf, z_itrf)).reshape((3, nrow)).T


def ecef_to_enu(r_ecef: np.ndarray) -> np.ndarray:
    """Rotation matrix from Earth-centered, Earth-fixed (ECEF) coordinates to East, North, Up (ENU) coordinates

    :param r_ecef: Point in Earth-fixed coordinates [km]
    :type r_ecef: np.ndarray [1x3]
    :return: Same point expressed in ENU coordinates
    :rtype: np.ndarray [1x3]
    """
    local_up_ecef = hat(r_ecef).reshape((1, 3))
    local_north_ecef = (
        np.array([[0, 0, 1]])
        - dot(local_up_ecef, np.array([[0, 0, 1]])) * local_up_ecef
    )
    local_east_ecef = np.cross(local_up_ecef, local_north_ecef)
    return np.vstack((local_east_ecef, local_north_ecef, local_up_ecef))


def lla_to_eci(
    lat_geod: float,
    lon: float,
    a: float,
    date: np.ndarray[datetime.datetime],
) -> np.ndarray:
    """Converts latitude, longitude, altitude (LLA) to Earth-centered inertial (ECI) coordinates

    :param lat_geod: Geodetic latitudes [rad]
    :type lat_geod: float
    :param lon: Longitudes [rad]
    :type lon: float
    :param a: Altitudes above the WGS84 ellipsoid [km]
    :type a: float
    :param date: Date to evaluate conversion [UTC]
    :type date: np.ndarray[datetime.datetime] [nx1]
    :return: ECI positions for each LLA triplet [km]
    :rtype:  np.ndarray [nx3]
    """
    r_itrf = lla_to_itrf(lat_geod, lon, a)
    date = np.array([date]).flatten()

    if date.size > 1:
        sidereal_rot = np.dstack([ecef_to_eci(d) for d in date])
        return stack_mat_mult(
            sidereal_rot, np.tile(r_itrf, (date.size, 1))
        )
    else:
        sidereal_rot = ecef_to_eci(date[0])
        return np.reshape(sidereal_rot @ r_itrf.T, (1, 3))
