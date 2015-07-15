# coding=utf-8
"""Developer feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
"""
'lat': 47.6204,
'lon': -122.3491
"""


@scenario(
    'features/developer.feature',
    'Receive client requests with all cached tiles'
)
def test_receive_client_requests_with_all_cached_tiles():
    """Receive client requests with all cached tiles."""
    pass


@scenario(
    'features/developer.feature',
    'Receive client requests with no cached tiles'
)
def test_receive_client_requests_with_no_cached_tiles():
    """Receive client requests with no cached tiles."""
    pass


@scenario(
    'features/developer.feature',
    'Receive client requests with partially cached tiles'
)
def test_receive_client_requests_with_partially_cached_tiles():
    """Receive client requests with partially cached tiles."""
    pass


@given('a client request')
def a_client_request(client_request):
    """a client request."""
    return client_request


@given('request contains tiles which are cached')
def request_contains_tiles_which_are_cached(client_request):
    """request contains tiles which are cached."""
    return client_request(-122.3491, 47.6204)


@given('request contains tiles which are partially cached')
def request_contains_tiles_which_are_partially_cached(client_request):
    """request contains tiles which are partially cached."""
    return client_request(-122.3291, 47.6004)


@given('request contains tiles which are uncached')
def request_contains_tiles_which_are_uncached(client_request):
    """request contains tiles which are uncached."""
    return client_request(-127.3491, 52.6204)


@given('the server contains cached tile storage')
def the_server_contains_cached_tile_storage(tile_cache):
    """the server contains cached tile storage."""
    assert len(tile_cache) is not 0


@when('the server checks cached tiles')
def the_server_checks_cached_tiles():
    """the server checks cached tiles."""
    pass


@then('combine cached and uncached data into response')
def combine_cached_and_uncached_data_into_response():
    """combine cached and uncached data into response."""
    pass


@then('the server will find all cached tiles')
def the_server_will_find_all_cached_tiles():
    """the server will find all cached tiles."""
    pass


@then('the server will find less than all cached tiles')
def the_server_will_find_less_than_all_cached_tiles():
    """the server will find less than all cached tiles."""
    pass


@then('the server will generate a response containing cached data')
def the_server_will_generate_a_response_containing_cached_data():
    """the server will generate a response containing cached data."""
    pass


@then('the server will generate the cached tiles')
def the_server_will_generate_the_cached_tiles():
    """the server will generate the cached tiles."""
    pass


@then('the server will not find cached tiles')
def the_server_will_not_find_cached_tiles():
    """the server will not find cached tiles."""
    pass


@then('the server will send back the response')
def the_server_will_send_back_the_response():
    """the server will send back the response."""
    pass
