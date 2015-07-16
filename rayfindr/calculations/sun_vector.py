from math import sin, cos, tan
import numpy
from Pysolar import GetAltitude, GetAzimuth


def get_azimuth(date, lat, lon):
    azimuth = GetAzimuth(lat, lon, date)
    if azimuth < -180:
        azimuth = abs(azimuth) - 180
    elif azimuth == -180:
        azimuth = 0
    else:
        azimuth = abs(azimuth - 180)
    return int(round(azimuth))


def get_altitude(date, lat, lon):
    return int(round(GetAltitude(lat, lon, date)))


# reference:
# http://www.powerfromthesun.net/Book/chapter03/chapter03.html#3.3.1 Simple Shadows
def get_sun_vector(altitude, azimuth):
    """Return a vector representing shadow projection of the sun.

    Inputs:
    sun_azimuth: int. Azimuth of the sun in degrees
    sun_altitude: int. Height of the sun in feet.

    Outputs:
    Tuple representing vector in format (longitude, latitude)
    """
    alt_rad = numpy.deg2rad(altitude)
    az_rad = numpy.deg2rad(azimuth)
    rad180 = numpy.deg2rad(180)
    magnitude = 1 / tan(alt_rad)
    vector_x = sin(az_rad - rad180) * magnitude
    vector_y = cos(az_rad - rad180) * magnitude
    return vector_x, vector_y
