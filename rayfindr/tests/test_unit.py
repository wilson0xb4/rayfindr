import pytest
import datetime
import rayfindr.calculations as calc


def test_receive_location(app):
    pass


def test_sun_location():
    pass


def test_building_data():
    pass


def test_get_azimuth():
    lat = 47.6062095
    lon = -122.3320708
    d_time = datetime(2015, 7, 16, 20)
    actual = calc.get_azimuth(d_time, lat, lon)
    assert actual > 140 and actual < 1458
