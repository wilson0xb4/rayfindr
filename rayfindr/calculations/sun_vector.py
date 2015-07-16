from math import sin, cos, tan
from Pysolar import GetAltitude, GetAzimuth


def get_azimuth(date, lat, lon):
    return GetAzimuth(lat, lon, date)


def get_altitude(date, lat, lon):
    return GetAltitude(lat, lon, date)


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
    # correct for library orientation
    if azimuth > 0:
        azimuth = abs(azimuth - 180)
    else:
        azimuth = abs(azimuth) + 180

    magnitude = 1 / tan(altitude)
    vector_x = cos(azimuth) * magnitude
    vector_y = sin(azimuth) * magnitude
    # convert from feet to lon / lat
    vector_x = (vector_x / 3280.4) * 0.009
    vector_y = (vector_y / 3280.4) * 0.009
    return vector_x, vector_y
