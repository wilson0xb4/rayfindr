# coding=utf-8
"""Developer feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/developer.feature', 'Receive client requests with all cached tiles')
def test_receive_client_requests_with_all_cached_tiles():
    """Receive client requests with all cached tiles."""
    pass


@scenario('features/developer.feature', 'Receive client requests with no cached tiles')
def test_receive_client_requests_with_no_cached_tiles():
    """Receive client requests with no cached tiles."""
    pass


@scenario('features/developer.feature', 'Receive client requests with partially cached tiles')
def test_receive_client_requests_with_partially_cached_tiles():
    """Receive client requests with partially cached tiles."""
    pass


@given('a client request')
def a_client_request():
    """a client request."""



@given('request contains tiles which are cached')
def request_contains_tiles_which_are_cached():
    """request contains tiles which are cached."""


@given('request contains tiles which are partially cached')
def request_contains_tiles_which_are_partially_cached():
    """request contains tiles which are partially cached."""


@given('request contains tiles which are uncached')
def request_contains_tiles_which_are_uncached():
    """request contains tiles which are uncached."""


@given('the server contains cached tile storage')
def the_server_contains_cached_tile_storage():
    """the server contains cached tile storage."""


@when('the server checks cached tiles')
def the_server_checks_cached_tiles():
    """the server checks cached tiles."""


@then('combine cached and uncached data into response')
def combine_cached_and_uncached_data_into_response():
    """combine cached and uncached data into response."""


@then('the server will find all cached tiles')
def the_server_will_find_all_cached_tiles():
    """the server will find all cached tiles."""


@then('the server will find less than all cached tiles')
def the_server_will_find_less_than_all_cached_tiles():
    """the server will find less than all cached tiles."""


@then('the server will generate a response containing cached data')
def the_server_will_generate_a_response_containing_cached_data():
    """the server will generate a response containing cached data."""


@then('the server will generate the cached tiles')
def the_server_will_generate_the_cached_tiles():
    """the server will generate the cached tiles."""


@then('the server will not find cached tiles')
def the_server_will_not_find_cached_tiles():
    """the server will not find cached tiles."""


@then('the server will send back the response')
def the_server_will_send_back_the_response():
    """the server will send back the response."""

