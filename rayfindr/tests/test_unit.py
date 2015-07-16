import pytest
from datetime import datetime
from rayfindr.calculations import sun_vector as sv


def test_receive_location():
    pass


def test_building_data():
    pass

azimuth_input_output = [
    [datetime(2015, 7, 16, 14), (70, 75)],
    [datetime(2015, 7, 16, 20), (170, 175)],
    [datetime(2015, 7, 17, 2), (280, 285)]
]


altitude_input_output = [
    [datetime(2015, 7, 16, 14), (10, 15)],
    [datetime(2015, 7, 16, 20), (60, 65)],
    [datetime(2015, 7, 17, 2), (15, 20)]
]


@pytest.mark.parametrize("date, az_range", azimuth_input_output)
def test_get_azimuth(date, az_range):
    lat = 47.6062095
    lon = -122.3320708
    d_time = date
    actual = sv.get_azimuth(d_time, lat, lon)
    az_low, az_high = az_range
    assert actual > az_low and actual < az_high


@pytest.mark.parametrize("date, alt_range", altitude_input_output)
def test_get_altitude(date, alt_range):
    lat = 47.6062095
    lon = -122.3320708
    d_time = date
    actual = sv.get_altitude(d_time, lat, lon)
    az_low, az_high = alt_range
    assert actual > az_low and actual < az_high
