import pytest
import requests
import json


@pytest.fixture()
def server():
    pass


@pytest.fixture()
def client():
    data = json.dumps({
        'year': 2015,
        'month': 7,
        'day': 15,
        'hour': 18,
        'lat': 47.6204,
        'lon': -122.3491
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
