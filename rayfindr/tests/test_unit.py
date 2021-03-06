from __future__ import unicode_literals

import os
import pytest
from datetime import datetime
from osgeo import ogr
from rayfindr.calculations import sun_vector as sv
from rayfindr.calculations import shadows as sh
from rayfindr.mapquery import spatial_filter, HERE


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
        prev_x, prev_y = curr_x, curr_y


def test_get_sun_vector_91_to_180():
    prev_x, prev_y = sv.get_sun_vector(60, 91)
    for deg in range(92, 181):
        curr_x, curr_y = sv.get_sun_vector(60, deg)
        assert prev_x < curr_x
        assert prev_y < curr_y
        prev_x, prev_y = curr_x, curr_y


def test_get_sun_vector_181_to_270():
    prev_x, prev_y = sv.get_sun_vector(60, 181)
    for deg in range(182, 271):
        curr_x, curr_y = sv.get_sun_vector(60, deg)
        assert prev_x < curr_x
        assert prev_y > curr_y
        prev_x, prev_y = curr_x, curr_y


def test_get_sun_vector_271_to_359():
    prev_x, prev_y = sv.get_sun_vector(60, 271)
    for deg in range(272, 360):
        curr_x, curr_y = sv.get_sun_vector(60, deg)
        assert prev_x > curr_x
        assert prev_y > curr_y
        prev_x, prev_y = curr_x, curr_y


def test_spatial_filter(num_unfiltered_features):
    shapefile = os.path.join(HERE, 'tests/code_fellows/code_fellows.shp')
    la_min, la_max, lo_min, lo_max = (47.6197, 47.6244, -122.3301, -122.3383)
    filtered = spatial_filter(
        la_min, la_max, lo_min, lo_max, datafile=shapefile
    )
    num_filtered_features = len(filtered)
    assert num_filtered_features < num_unfiltered_features

    sorted_height = sorted(filtered, key=lambda feat: feat[0])
    tallest = sorted_height[-1]
    assert tallest[0] == 277


def test_shadow_from_points(sun_vector, feature_tuples):
    height, footprint = feature_tuples[0]
    output = sh.get_shadow_from_points(sun_vector, height, footprint)
    assert isinstance(output, ogr.Geometry)


def test_get_shadow_from_data(sun_vector, feature_tuples):
    output = sh.get_shadow_from_data(sun_vector, feature_tuples)
    assert output['type'] == 'MultiPolygon'
    assert 'coordinates' in output
