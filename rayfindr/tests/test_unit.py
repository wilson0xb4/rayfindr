import pytest
from datetime import datetime
from rayfindr.calculations import sun_vector as sv


def test_receive_location():
    pass


def test_sun_location():
    pass


def test_building_data():
    pass


def test_get_azimuth():
    lat = 47.6062095
    lon = -122.3320708
    d_time = datetime(2015, 7, 16, 20)
    actual = sv.get_azimuth(d_time, lat, lon)
    assert actual > 140 and actual < 1458
