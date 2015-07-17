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


@pytest.fixture()
def feature_tuples():
    tuples = [
        (104,
         [[[-122.3341081676428, 47.622807672154515],
           [-122.33371396605794, 47.622808880605135],
           [-122.33371013502375, 47.62220739577516],
           [-122.33378438657446, 47.622207168081026],
           [-122.33402927419269, 47.622206416876246],
           [-122.33411047230933, 47.622206167544],
           [-122.33411410394847, 47.62264094511944],
           [-122.33414749921288, 47.62264081782053],
           [-122.33414845705191, 47.62275547190794],
           [-122.33411506040973, 47.62275560012394],
           [-122.33411549619568, 47.622807651086056],
           [-122.3341081676428, 47.622807672154515]]]),
        (95,
         [[[-122.33450206826922, 47.62293921155707],
           [-122.33449198514617, 47.62244923813805],
           [-122.3344976169109, 47.62244902621719],
           [-122.33489086367565, 47.6224504193843],
           [-122.33489059306284, 47.62242836636449],
           [-122.33496797141328, 47.62242793651991],
           [-122.33496824072883, 47.622449989557104],
           [-122.33508885768481, 47.62244932019757],
           [-122.33509566676359, 47.62244928252989],
           [-122.33513494065988, 47.62244906387738],
           [-122.33513499843478, 47.622457794711266],
           [-122.33513578562754, 47.62250833960045],
           [-122.3351398672653, 47.622854422552024],
           [-122.33514023714181, 47.622884703877475],
           [-122.33514023973939, 47.62289083197352],
           [-122.33513876112748, 47.62294175490831],
           [-122.33512760454065, 47.62294095483334],
           [-122.33490256960351, 47.62294028864379],
           [-122.33450206826922, 47.62293921155707]]]),
        (86,
         [[[-122.334503654228, 47.62306688998667],
           [-122.33450206826922, 47.62293921155707],
           [-122.33490256960351, 47.62294028864379],
           [-122.33490417004937, 47.62310254872208],
           [-122.33489754060972, 47.62310258940485],
           [-122.33455222303388, 47.623104524095915],
           [-122.3345519220514, 47.62307721776763],
           [-122.33450378650701, 47.62307746853098],
           [-122.334503654228, 47.62306688998667]]])
    ]
    return tuples
