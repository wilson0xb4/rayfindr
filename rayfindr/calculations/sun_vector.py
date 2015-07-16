from math import sin, cos, tan
from Pysolar import GetAltitude, GetAzimuth
from datetime import datetime


# reference:
# http://www.powerfromthesun.net/Book/chapter03/chapter03.html#3.3.1 Simple Shadows
def get_sun_vector(year, month, day, hour, lat, lon):
    """Return a vector representing shadow projection of the sun.

    Inputs:
    sun_azimuth: int. Azimuth of the sun in degrees
    sun_altitude: int. Height of the sun in feet.

    Outputs:
    Tuple representing vector in format (longitude, latitude)

    1 degrees = 0.0174532925 radians
    """
    d_time = datetime(year, month, day, hour)
    sun_azimuth = GetAzimuth(lat, lon, d_time)
    # correct for library orientation
    if sun_azimuth > 0:
        sun_azimuth = abs(sun_azimuth - 180)
    else:
        sun_azimuth = abs(sun_azimuth) + 180
    sun_altitude = GetAltitude(lat, lon, d_time)

    magnitude = 1 / tan(sun_altitude)
    vx = cos(sun_azimuth) * magnitude
    vy = sin(sun_azimuth) * magnitude
    # convert from feet to lon / lat
    vx = (vx / 3280.4) * 0.009
    vy = (vy / 3280.4) * 0.009
    return vx, vy
