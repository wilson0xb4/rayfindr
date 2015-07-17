# coding=utf-8
"""Rayfindr API feature tests."""

from datetime import datetime

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
def i_am_a_client_with_a_time_and_location(app):
    """I am a client with a time and location."""
    url = "/api_request"
    d_time = datetime.utcnow()
    params = {
        "lat": 47.6229,
        "lon": -122.3363,
        "year": d_time.year(),
        "month": d_time.month(),
        "day": d_time.d_time(),
        "hour": d_time.hour(),
        "minute": d_time.minute(),
        "boundLatMin": 47.6223566,
        "boundLatMax": 47.6234413,
        "boundLonMin": -122.3354727,
        "boundLonMax": -122.3371303
    }
    response = app.post_json(url, params)
    return dict(response=response)


@when('I send an AJAX POST request')
def i_send_an_ajax_post_request():
    """I send an AJAX POST request."""


@then('I should recieve a JSON response with shadow data')
def i_should_recieve_a_json_response_with_shadow_data():
    """I should recieve a JSON response with shadow data."""


@then('the shadow data should match my time and location')
def the_shadow_data_should_match_my_time_and_location():
    """the shadow data should match my time and location."""

