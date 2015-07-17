import json
import os
import pytest
import requests

from osgeo import ogr
from rayfindr.mapquery import HERE


@pytest.fixture()
def client_request(lat, lon):
    data = json.dumps({
        'year': 2015,
        'month': 7,
        'day': 15,
        'hour': 18,
        'lat': lat,
        'lon': lon
    })

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest'
    }

    r = requests.post(
        'http://rayfindr.com/api_request',
        data=data,
        headers=headers
    )

    return r


@pytest.fixture()
def num_unfiltered_features():
    shapefile = os.path.join(HERE, 'tests/code_fellows/code_fellows.shp')
    driver = ogr.GetDriverByName('ESRI Shapefile')
    datasource = driver.Open(shapefile)
    layer = datasource.GetLayer()
    feature_count = layer.GetFeatureCount()
    return feature_count
