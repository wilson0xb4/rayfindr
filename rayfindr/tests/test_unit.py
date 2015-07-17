import pytest
from datetime import datetime
from rayfindr.calculations import sun_vector as sv


azimuth_in_out = [
    [datetime(2015, 7, 16, 14), (70, 75)],
    [datetime(2015, 7, 16, 20), (170, 175)],
    [datetime(2015, 7, 17, 2), (280, 285)]
]


altitude_in_out = [
    [datetime(2015, 7, 16, 14), (10, 15)],
    [datetime(2015, 7, 16, 20), (60, 65)],
    [datetime(2015, 7, 17, 2), (15, 20)]
]


@pytest.mark.parametrize("date, az_range", azimuth_in_out)
def test_get_azimuth(date, az_range):
    lat = 47.6062095
    lon = -122.3320708
    d_time = date
    actual = sv.get_azimuth(d_time, lat, lon)
    az_low, az_high = az_range
    assert actual > az_low and actual < az_high


@pytest.mark.parametrize("date, alt_range", altitude_in_out)
def test_get_altitude(date, alt_range):
    lat = 47.6062095
    lon = -122.3320708
    d_time = date
    actual = sv.get_altitude(d_time, lat, lon)
    az_low, az_high = alt_range
    assert actual > az_low and actual < az_high


def test_get_sun_vector_0_to_90():
    prev_x, prev_y = sv.get_sun_vector(60, 0)
    for deg in range(1, 91):
        curr_x, curr_y = sv.get_sun_vector(60, deg)
        assert prev_x > curr_x
        assert prev_y < curr_y


def test_get_sun_vector_91_to_180():
    prev_x, prev_y = sv.get_sun_vector(60, 91)
    for deg in range(92, 181):
        curr_x, curr_y = sv.get_sun_vector(60, deg)
        assert prev_x < curr_x
        assert prev_y < curr_y


def test_get_sun_vector_181_to_270():
    prev_x, prev_y = sv.get_sun_vector(60, 181)
    for deg in range(182, 271):
        curr_x, curr_y = sv.get_sun_vector(60, deg)
        assert prev_x < curr_x
        assert prev_y > curr_y


def test_get_sun_vector_271_to_359():
    prev_x, prev_y = sv.get_sun_vector(60, 271)
    for deg in range(272, 360):
        curr_x, curr_y = sv.get_sun_vector(60, deg)
        assert prev_x > curr_x
        assert prev_y > curr_y


def test_spatial_filter():
    pass


def test_get_shadow_from_data():
    pass


def test_shadow_from_points():
    pass
