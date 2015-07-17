from math import sin, cos, tan, radians
from Pysolar import GetAltitude, GetAzimuth


def get_azimuth(date, lat, lon):
    """
    Return the horizontal position of the sun as azimuth in degrees, North
    being 0 and increasing positively to 359 in clockwise rotation.

    Inputs:
        Date: UTC Timezone representation of current date/time. Currently
        calculates to the minute.
        Lat: Current latitude provided by HTML5 location data from client.
        Lon: Current longitude provided by HTML5 location data from client.
    """
    azimuth = GetAzimuth(lat, lon, date)
    if azimuth < -180:
        azimuth = abs(azimuth) - 180
    elif azimuth == -180:
        azimuth = 0
    else:
        azimuth = abs(azimuth - 180)
    return int(round(azimuth))


def get_altitude(date, lat, lon):
    """
    Return the altitude of the sun from the horizon in degrees.

    Inputs:
        Date: UTC Timezone representation of current date/time. Currently
        calculates to the minute.
        Lat: Current latitude provided by HTML5 location data from client.
        Lon: Current longitude provided by HTML5 location data from client.
    """
    return int(round(GetAltitude(lat, lon, date)))


def get_sun_vector(altitude, azimuth):
    """reference:
    powerfromthesun.net/Book/chapter03/chapter03.html#3.3.1 Simple Shadows"""

    """Return a vector representing shadow projection of the sun.

    Inputs:
    sun_azimuth: int. Azimuth of the sun in degrees
    sun_altitude: int. Height of the sun in feet.

    Outputs:
    Tuple representing vector in format (longitude, latitude)
    """
    alt_rad = radians(altitude)
    az_rad = radians(azimuth)
    rad180 = radians(180)
    magnitude = 1 / tan(alt_rad)
    vector_x = sin(az_rad - rad180) * magnitude
    vector_y = cos(az_rad - rad180) * magnitude
    return vector_x, vector_y
