# coding=utf-8
"""Rayfindr API feature tests."""

from datetime import datetime
import json

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/developer.feature', 'Client connects to API')
def test_client_connects_to_api():
    """Client connects to API."""
    pass


@given('I am a client with a time and location')
def i_am_a_client_with_a_time_and_location():
    """I am a client with a time and location."""
    url = "/api_request"
    d_time = datetime.utcnow()
    year = d_time.year
    month = d_time.month
    day = d_time.day
    hour = d_time.hour
    minute = d_time.minute

    params = {
        "lat": 47.6229,
        "lon": -122.3363,
        "year": year,
        "month": month,
        "day": day,
        "hour": hour,
        "minute": minute,
        "boundLatMin": 47.6223566,
        "boundLatMax": 47.6234413,
        "boundLonMin": -122.3354727,
        "boundLonMax": -122.3371303
    }
    params = json.dumps(params)
    return dict(url=url, params=params, response='')


@when('I send an AJAX POST request')
def i_send_an_ajax_post_request(i_am_a_client_with_a_time_and_location, app):
    """I send an AJAX POST request."""
    client = i_am_a_client_with_a_time_and_location
    url = client['url']
    params = client['params']
    response = app.post(url, params, xhr=True)
    client['response'] = response


@then('I should recieve a JSON response with shadow data')
def i_should_recieve_a_json_response_with_shadow_data(i_am_a_client_with_a_time_and_location):
    """I should recieve a JSON response with shadow data."""
    response = i_am_a_client_with_a_time_and_location['response']
    assert response.status_code == 200
    body = json.loads(response.body)
    assert body['type'] == 'MultiPolygon'
    assert 'coordinates' in body
