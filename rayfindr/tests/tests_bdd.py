# _*_ coding: utf-8- _*_
from __future__ import unicode_literals
from pytest_bdd import scenario, given, when, then
# import pytest


@scenario('features/developer.feature', 'Receive incoming client request')
def test_incoming_request():
    pass


@given('A client has made a request to the server')
def inbound_reqeust():
    pass


@when('the request contains location data')
def location_data_present():
    pass


@then('the server will generate requests to external APIs')
def api_request():
    pass


@scenario('features/developer.feature', 'Use client location to generate sun location data')
def test_sun_location_data():
    pass


@given('the client has provided location data')
def location_time_present():
    pass


@when('a request has been received')
def inbound_request():
    pass


@then('the server will generate map data and send a response')
def send_response():
    pass


@scenario('features/developer.feature', 'Return data to client')
def test_response_data():
    pass


@given('the client has provided data')
def client_request_with_data():
    pass


@then('the server has generated a response')
def response_data_package():
    pass


@then('sent response back to client')
def send_data_package():
    pass


@scenario('features/client.feature', 'Generate and Send location data to server')
def test_generate_send_location_data():
    pass


@given('The user opens the client web page')
def page_load():
    pass


@given('the client allows location tracking')
def location_tracking_available():
    pass


@then('the browser sends a location data package to the server')
def location_sent_to_server():
    pass


@scenario('features/client.feature', 'Receive sun location from server')
def test_receive_data_from_server():
    pass


@given('a location data package has been sent to the server')
def data_sent_to_server():
    pass


@when('the user opens the client web page')
def unrendered_map_present():
    pass


@then('the client receives a data package from the server')
def received_data_package():
    pass


@then('updates the client map software with Sun location data points')
def render_map_box_shadows():
    pass
