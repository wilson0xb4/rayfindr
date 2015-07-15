from math import sin, cos, tan


# reference:
# http://www.powerfromthesun.net/Book/chapter03/chapter03.html#3.3.1 Simple Shadows
def get_sun_vector(sun_azimuth, sun_altitude):
    """Return a vector representing shadow projection of the sun.

    Inputs:
    sun_azimuth: int. Azimuth of the sun in degrees
    sun_altitude: int. Height of the sun in feet.

    Outputs:
    Tuple representing vector in format (longitude, latitude)
    """
    magnitude = 1 / tan(sun_altitude)
    vx = cos(sun_azimuth) * magnitude
    vy = sin(sun_azimuth) * magnitude
    # convert from feet to lon / lat
    vx = (vx / 3280.4) * 0.009
    vy = (vy / 3280.4) * 0.009
    return vx, vy
