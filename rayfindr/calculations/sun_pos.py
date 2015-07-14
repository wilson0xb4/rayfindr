#  coding=utf8

# sunpos - Compute the position of the sun relative to
# Earth's orbit, according to the current date and time and
# the observer's position on Earth.
#
# Aaron Mansheim 2011-06-22
#
# Based closely on: http://stjarnhimlen.se/comp/tutorial.html 2009-07-02
# Note that sunriset.c by the same author is in the public domain,
# so I believe I'm not taking anything that he doesn't willingly give.
#
# Ultimately my purpose is to make this as clear as possible to 
# anyone who understands a) basics of the Python programming language
# and b) how the sine and cosine functions relate to a point on
# the circumference of the unit circle.

from math import sqrt, hypot, floor, atan2, asin, cos, sin, pi, fsum


def sind(x):
    return sin(x * pi / 180)


def cosd(x):
    return cos(x * pi / 180)


def adtan2(y, x):
    return ((180 / pi) * atan2(y, x))


def adsin(x):
    return ((180 / pi) * asin(x))


def rev(x):
    return (x - floor(x / 360.0) * 360.0)


def polar_to_cartesian2d(r, theta):
    x = r * cosd(theta)
    y = r * sind(theta)
    return (x, y)


def cartesian2d_to_polar(x, y):
    r = hypot(x, y)
    theta = rev(adtan2(y, x))
    return (r, theta)


def rotate_polar(r, theta, delta_theta):
    return (r, rev(theta + delta_theta))


def spherical_to_cylindrical(radius, latitude, longitude):
    (cylindrical_radius, height) = polar_to_cartesian2d(radius, latitude)
    return (cylindrical_radius, height, longitude)


def cylindrical_to_cartesian3d(radius, height, longitude):
    (x, y) = polar_to_cartesian2d(radius, longitude)
    z = height
    return (x, y, z)


def spherical_to_cartesian3d(radius, latitude, longitude):
    (x, y, z) = cylindrical_to_cartesian3d(*spherical_to_cylindrical(
        radius,
        latitude,
        longitude,
    ))
    return (x, y, z)


def cartesian3d_to_cylindrical(x, y, z):
    (cylindrical_radius, longitude) = cartesian2d_to_polar(x, y)
    height = z
    return (cylindrical_radius, height, longitude)


def cylindrical_to_spherical(cylindrical_radius, height, longitude):
    (radius, latitude) = cartesian2d_to_polar(cylindrical_radius, height)
    return (radius, latitude, longitude)


def cartesian3d_to_spherical(x, y, z):
    (
        r,
        latitude,
        longitude,
    ) = cylindrical_to_spherical(*cartesian3d_to_cylindrical(x, y, z))
    return (r, latitude, longitude)


def rotate_cartesian3d_about_x(x, y, z, theta):
    (x, y, z) = (x, ) + polar_to_cartesian2d(*rotate_polar(
            *(cartesian2d_to_polar(y, z) + (theta, ))
    ))
    return (x, y, z)


def decline_cartesian3d_about_y(x, y, z, theta):
    # Equivalent to:
    # (lambda neg_y, x, z: (x, -neg_y, z)) (
    #   *rotate_cartesian3d_about_x(-y, x, z, 90 - theta)
    # )
    # We could have written (y, x, z), but (-y, x, z) has the
    # nice property that it is just (x, y, z) rotated around z.

    (xhor, zhor) = polar_to_cartesian2d(*rotate_polar(
            *(cartesian2d_to_polar(x, z) + (90 - theta, ))
    ))
    return (xhor, y, zhor)


def day_number(Y, M, D):
    """
    This formula models the common astronomical calendar,
    which coincides with the Gregorian calendar for years 1901-2099.
    On the other hand it is actually a Julian calendar in that it has
    no exceptions to the rule that every fourth year is a leap year.
    """
    return (
        367 * Y
        - (7 * (Y + (M + 9) // 12)) // 4
        + (275 * M) // 9
        + D
        - 730530)


def sun_earth_elements(day_number):
    """
    Why this function is named "sun_earth_elements":
    We're primarily concerned with the Earth-based observer,
    so we'll use these orbital elements to determine how the Sun
    moves through Earth's sky. Of course, outside of that frame
    it is more sensible to interpret these elements vice versa,
    with Earth moving around the Sun.
    """

    w = rev(282.9404 + 4.70935E-5 * day_number)    # longitude of perihelion
    a = 1.000000                                   # mean_distance, in a.u.
    e = 0.016709 - 1.151E-9 * day_number           # eccentricity
    M = rev(356.0470 + 0.9856002585 * day_number)  # mean anomaly
    return (w, a, e, M)


def ecliptic_anomaly_to_longitude(
        longitude_of_periapsis,
        angle_from_periapsis,
):
    """
    Ecliptic longitude, sometimes written simply as
    "longitude", has its zero at the ascending node.
    For the Sun-Earth system, the ascending node is
    the vernal point (if I'm not mistaken!?).
    In contrast to longitude, the mean anomaly and true
    anomaly have their zero at periapsis. For the
    Sun-Earth system, the periapsis is perihelion.
    When we say "mean longitude" of the Sun, we mean
    "mean ecliptic longitude" with zero longitude at the
    vernal point. We are not referring to the terrestrial
    longitude or to the celestial longitude (also known
    as right ascension) that are zero at a meridian.
    We should also explain "mean longitude" vs. "longitude".
    The mean longitude progresses quite cyclically,
    while the (true) longitude goes elliptically.
    Both complete one revolution in the same time.
    True longitude measures the actual accelerating
    and decelerating position of a body. Mean longitude
    averages out the position over the whole revolution
    to measure out a fictitious steady motion.
    """
    return rev(longitude_of_periapsis + angle_from_periapsis)


def obliquity_of_the_ecliptic(day_number):
    """
    Inclination of Earth's axis of rotation
    to its plane of revolution.
    """
    return 23.4393 - 3.563E-7 * day_number


def eccentric_anomaly_first_approximation(mean_anomaly, eccentricity):
    """
    This truncated Taylor series is claimed accurate enough for a small
    eccentricity such as that of the Sun-Earth orbit (0.017).
    Properly the eccentric anomaly is the solution E
    of Kepler's equation in mean anomaly M and eccentricity e:
        M = E - e sin(E).
    Thanks to Paul Schlyter himself for clarifying this in a
    private email which, frankly, I have not yet fully analyzed.
    """
    return rev(
        mean_anomaly
        + (180 / pi) * eccentricity * sind(mean_anomaly)
        * (1 + eccentricity * cosd(mean_anomaly)))

    # Note if we write E(n+1) = M + e sin (E(n)) and iterate,
    # we get this, which is supposedly equivalent!?
    # E(1) = M + e sin (E(0))
    # E(2) = M + e sin ( M + e sin (E(0)) )
    #      = M + e sin (M) cos (e sin (E(0))) + e cos (M) sin (e sin (E(0)) )
    # E(3) = M + e sin ( M + e sin ( M + e sin ( E(0) ) ) )


def eccentric_to_cartesian2d(eccentric_anomaly, eccentricity):
    # This would be easy to understand from a simple diagram.
    x = cosd(eccentric_anomaly) - eccentricity
        # == radius * cosd(theta)
    y = sind(eccentric_anomaly) * sqrt(1 - eccentricity ** 2)
        # == radius * sind(theta)
    return (x, y)


def arcdegrees_to_arcminutes(d):
    return 60 * d


# return: (distance, true_longitude, mean_longitude, oblecl, )
def date_to_sun_earth_ecliptic(Y, Month, D):

    # return: (w, a, e, M, oblecl, )
    def sun_earth_elements_and_oblecl(Y, Month, D):
        d = day_number(Y, Month, D)
        return sun_earth_elements(d) + (obliquity_of_the_ecliptic(d), )

    # return: (distance, ecliptic_angle, )
    def ecliptic_polar(M, e):
        return cartesian2d_to_polar(* eccentric_to_cartesian2d(
            eccentric_anomaly_first_approximation(M, e),
            e,
        ))

    # return: (distance, true_longitude, mean_longitude, oblecl, )
    def longitudes(M, e, w, oblecl):
        (distance, true_anomaly) = ecliptic_polar(M, e)
        return (
            distance,
            ecliptic_anomaly_to_longitude(w, true_anomaly),
            ecliptic_anomaly_to_longitude(w, M),
            oblecl,
        )

    # return: (distance, true_longitude, mean_longitude, oblecl, )
    def date_to_sun_earth_ecliptic_1(Y, Month, D):
        (w, a_ignored, e, M, oblecl, ) = sun_earth_elements_and_oblecl(
            Y,
            Month,
            D,
        )
        return longitudes(M, e, w, oblecl)

    return date_to_sun_earth_ecliptic_1(Y, Month, D)


def arcdegrees_to_hours(d):
    return d * 24 / 360.0


def sun_earth_ecliptic_to_celestial(distance, true_lon, oblecl):
    # equivalent to:
    # ecliptic_to_celestial(distance, 0.0, true_lon, oblecl)
    (distance1, Decl, RA) = cartesian3d_to_spherical(
        *rotate_cartesian3d_about_x(
            *(polar_to_cartesian2d(distance, true_lon) + (0.0, oblecl, ))
        )
    )
    return (distance1, Decl, RA)


def hours_to_seconds(h):
    return 3600 * h


def minutes_to_seconds(m):
    return 60 * m


def arcdegrees_to_arcseconds(d):
    return 3600 * d


def seconds_to_minutes(s):
    return s / 60.0


def GMST0(mean_longitude):
    """
    Sidereal time (in other words, right ascension in hours)
    at the 00:00 meridian at Greenwich right now.
    """
    return arcdegrees_to_hours(rev(mean_longitude + 180))


def sidereal_time(GMST0, UT, terrestrial_longitude):
    """
    Locally adjusted sidereal time: more info at function GMST0.
    """
    # TODO: normalize to 24 hours
    return GMST0 + UT + arcdegrees_to_hours(terrestrial_longitude)


def hour_angle(sidereal_time, RA):
    # TODO: normalize to 24 hours
    return sidereal_time - RA


def hours_to_arcdegrees(h):
    return rev(h * 360 / 24.0)


def sun_earth_celestial_to_alt_azimuth(mlon, Decl, RA, hours_UT, lat, lon):
    (distance, altitude, azimuth) = cartesian3d_to_spherical(
        *decline_cartesian3d_about_y(
            *(spherical_to_cartesian3d(
                1.0,
                Decl,
                hours_to_arcdegrees(hour_angle(
                    sidereal_time(GMST0(mlon), hours_UT, lon),
                    arcdegrees_to_hours(RA),
                )),
            ) + (lat, ))
        )
    )
    azimuth = rev(azimuth + 180)
    return (altitude, azimuth)


def time_and_location_to_sun_alt_azimuth(Y, M, D, hours_UT, lat, lon):

    def sun_earth_ecliptic_to_celestial_for_alt_azimuth(
        distance0,
        true_longitude,
        mean_longitude,
        oblecl,
    ):
        return (mean_longitude, ) + sun_earth_ecliptic_to_celestial(
            distance0,
            true_longitude,
            oblecl,
        )[1:3] + (hours_UT, lat, lon, )

    (altitude, azimuth) = sun_earth_celestial_to_alt_azimuth(
        *sun_earth_ecliptic_to_celestial_for_alt_azimuth(
            *date_to_sun_earth_ecliptic(
                Y,
                M,
                D,
            )
        )
    )

    return (altitude, azimuth)


def moon_elements(d):
    N = rev(125.1228 - 0.0529538083 * d)   # Long asc. node
    i = 5.1454                             # Inclination
    w = rev(318.0634 + 0.1643573223 * d)   # Arg. of perigee
    a = 60.2666                            # Mean distance,
                                           #   in Earth equatorial radii
    e = 0.054900                           # Eccentricity
    M = rev(115.3654 + 13.0649929509 * d)  # Mean anomaly
    return (N, i, w, a, e, M)


def iterate_for_eccentric_anomaly(M, e, E0):

    def iterate_once_for_eccentric_anomaly(M, e, E0):
        return E0 - (E0 - (180 / pi) * e * sind(E0) - M) / (1 - e * cosd(E0))

    """
    Approximately invert Kepler's equation M = E - e sin E
    by Newton's method.
    """
    E1 = E0
    E0 = 0
    k = 0
    while abs(E1 - E0) >= 0.005 and k < 30:
        k = k + 1
        E0 = E1
        E1 = iterate_once_for_eccentric_anomaly(M, e, E0)
    return E1


def cartesian2d_in_plane_of_orbit(eccentric_anomaly, eccentricity, distance):
    (x, y) = (
        distance * (cosd(eccentric_anomaly) - eccentricity),
        distance * sqrt(1 - eccentricity ** 2) * sind(eccentric_anomaly),
    )
    return (x, y)


def position_from_plane_of_orbit_to_ecliptic(r, theta, N, i, w):
    # TODO: break this down to easily understood operations
    #   using angle sum formulas etc.
    #                           _ _     _ _     _
    # cos(-x) = cos(x)        1 |X \   /|X \   /| cos
    # sin(-x) = -sin(x)       0 /-\-\-/-/-\-\-/-/ sin
    # sin(x) = cos(x - 90)   -1 |  \_X_/|  \_X_/|
    # sin(x - 90) = -cos(x)    -2pi     0       2pi
    #                           _ _     _ _     _
    #                         1 ┆╳ ╲   ╱┆╳ ╲   ╱┆ cos
    #                         0 ╱┄╲┄╲┄╱┄╱┄╲┄╲┄╱┄╱ sin
    #                        -1 ┆  ╲_╳_╱┆  ╲_╳_╱┆
    #                          -2pi     0       2pi
    # a - b = a + (-b)
    # cos(a + b) = cos(a)cos(b) - sin(a)sin(b)
    # cos(a - b) = cos(a)cos(b) + sin(a)sin(b)
    # sin(a + b) = sin(a)cos(b) + cos(a)sin(b)
    # sin(a - b) = sin(a)cos(b) - cos(a)sin(b)

    (xeclip, yeclip, zeclip) = (
        r * (
            cosd(N) * cosd(theta + w)
            - sind(N) * sind(theta + w) * cosd(i)
        ),
        r * (
            sind(N) * cosd(theta + w)
            + cosd(N) * sind(theta + w) * cosd(i)
        ),
        r * sind(theta + w) * sind(i),
    )
    return (xeclip, yeclip, zeclip)


def moon_perturbation_arguments(mlon, moon_N, moon_w, moon_M, M):
    Lm = moon_N + moon_w + moon_M
    (
        Ls,  # Sun's mean longitude
        Ms,  # Sun's mean anomaly
        Mm,  # Moon's mean anomaly
        D,   # Moon's mean elongation
        F,   # Moon's argument of latitude
    ) = (
        mlon,
        M,
        moon_M,
        rev(Lm - mlon),
        rev(Lm - moon_N),
    )
    return (Ls, rev(Lm), Ms, Mm, D, F)


def moon_12_longitude_perturbation_terms(Ls, Lm, Ms, Mm, D, F):
    # All & only the terms larger than 0.01 degrees,
    # aiming for 1-2 arcmin accuracy.
    # Even with the first two terms the error is usually under 0.25 degree.
    # These might come from EPL.
    return (
        -1.274 * sind(Mm - 2 * D),      # Evection (Ptolemy)
        +0.658 * sind(2 * D),           # Variation (Tycho Brahe)
        -0.186 * sind(Ms),              # Yearly equation (Tycho Brahe)
        -0.059 * sind(2 * Mm - 2 * D),
        -0.057 * sind(Mm - 2 * D + Ms),
        +0.053 * sind(Mm + 2 * D),
        +0.046 * sind(2 * D - Ms),
        +0.041 * sind(Mm - Ms),
        -0.035 * sind(D),               # Parallactic equation
        -0.031 * sind(Mm + Ms),
        -0.015 * sind(2 * F - 2 * D),
        +0.011 * sind(Mm - 4 * D),
    )


def moon_5_latitude_perturbation_terms(Ls, Lm, Ms, Mm, D, F):
    # All & only the terms larger than 0.01 degrees
    # aiming for 1-2 arcmin accuracy.
    # Even with the first term the error is usually under 0.15 degree.
    return (
        -0.173 * sind(F - 2 * D),
        -0.055 * sind(Mm - F - 2 * D),
        -0.046 * sind(Mm + F - 2 * D),
        +0.033 * sind(F + 2 * D),
        +0.017 * sind(2 * Mm + F),
    )


def moon_2_distance_perturbation_terms(Ls, Lm, Ms, Mm, D, F):
    # all & only the terms larger than 0.1 Earth radii
    return (
        -0.58 * cosd(Mm - 2 * D),
        -0.46 * cosd(2 * D),
    )


def date_and_sun_mean_to_moon_ecliptic(Y, Month, D, mean_longitude, mean_anomaly):
    # TODO: Generalize. Much of this is not specific to the moon.

    def moon_elliptic_to_polar(a, e, M):
        return cartesian2d_to_polar(*cartesian2d_in_plane_of_orbit(
            iterate_for_eccentric_anomaly(
                M,
                e,
                eccentric_anomaly_first_approximation(M, e)
            ),
            e,
            a
        ))

    def moon_elements_to_spherical(N, i, w, a, e, M):
        return cartesian3d_to_spherical(
            *position_from_plane_of_orbit_to_ecliptic(
                *(moon_elliptic_to_polar(a, e, M) + (N, i, w, ))
            )
        )

    def moon_elements_to_spherical_perturbation(N, i, w, a, e, M):
        return map (
            fsum,
            (lambda args : (
                moon_2_distance_perturbation_terms(*args),
                moon_5_latitude_perturbation_terms(*args),
                moon_12_longitude_perturbation_terms(*args),
            )) (moon_perturbation_arguments(
                mean_longitude,
                N,
                w,
                M,
                mean_anomaly,
            )),
        )

    def date_and_sun_mean_to_moon_ecliptic_1(Y, Month, D):
        return map(sum, zip(
            *(lambda elems: (
                moon_elements_to_spherical(*elems),
                moon_elements_to_spherical_perturbation(*elems),
            )) (moon_elements(day_number(Y, Month, D)))
        ))
    
    (pdist, plat, plon) = date_and_sun_mean_to_moon_ecliptic_1(Y, Month, D)
    return (pdist, plat, plon)


def ecliptic_to_celestial(distance, latitude, longitude, oblecl):
    (distance1, Decl, RA) = cartesian3d_to_spherical(
        *rotate_cartesian3d_about_x(
            *(
                spherical_to_cartesian3d(distance, latitude, longitude)
                + (oblecl, )
            )
        )
    )
    return (distance1, Decl, RA)
