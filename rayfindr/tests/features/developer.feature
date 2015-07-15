Feature: Developer
    Provide user API with access to geolocation data that renders sunny areas in real time on a map.


Scenario: Receive client requests with no cached tiles
    Given a client request
    And request contains tiles which are uncached
    And the server contains cached tile storage
    When the server checks cached tiles
    Then the server will not find cached tiles
    And the server will generate the cached tiles
    And the server will send back the response

Scenario: Receive client requests with partially cached tiles
    Given a client request
    And request contains tiles which are partially cached
    And the server contains cached tile storage
    When the server checks cached tiles
    Then the server will find less than all cached tiles
    And the server will generate the cached tiles
    And combine cached and uncached data into response
    And the server will send back the response

Scenario: Receive client requests with all cached tiles
    Given a client request
    And request contains tiles which are cached
    And the server contains cached tile storage
    When the server checks cached tiles
    Then the server will find all cached tiles
    And the server will generate a response containing cached data
    And the server will send back the response
