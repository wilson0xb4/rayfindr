from math import pi, sin, cos, tan, asin, atan2

rad = pi / 180
day_ms = 86400000
j1970 = 2440588
j2000 = 2451545
e = rad * 23.4397


def to_julian(date):
    return date / day_ms - 0.5 + j1970


def to_days(date):
    return to_julian(date) - j2000


def get_right_ascension(l, b):
    return atan2(sin(l) * cos(e) - tan(b) * sin(e), cos(l))


def get_declination(l, b):
    return asin(sin(b) * cos(e) + cos(b) * sin(e) * sin(l))


def get_azimuth(h, phi, dec):
    return atan2(sin(h), cos(h) * sin(phi) - tan(dec) * cos(phi))


def get_altitude(h, phi, dec):
    return asin(sin(phi) * sin(dec) + cos(phi) * cos(dec) * cos(h))


def get_side_real_time(d, lw):
    return rad * (280.16 + 360.9856235 * d) - lw


def get_solar_mean_anomoly(d):
    return rad * (357.5291 + 0.98560028 * d)


def get_equation_of_center(m):
    return rad * (
        1.9148 * sin(m) + 0.0200 * sin(2 * m) + 0.0003 * sin(3 * m)
    )


def get_ecliptic_longitude(m, c):
    p = rad * 102.9372
    return m + c + p + pi


def get_sun_position(date, lat, lon):
    lw = rad * -lon
    phi = rad * lat
    days = to_days(date)
    mean = get_solar_mean_anomoly(days)
    ctr = get_equation_of_center(mean)
    e_long = get_ecliptic_longitude(mean, ctr)
    dec = get_declination(e_long, 0)
    ascen = get_right_ascension(e_long, 0)
    time = get_side_real_time(days, lw)
    h = time - ascen

    return {
        'altitude': get_altitude(h, phi, dec),
        'azimuth': get_azimuth(h, phi, dec) - pi / 2
    }
