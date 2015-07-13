Feature: Developer
    Provide user api with access to geolocation data that renders sunny areas in real time on a map.


Scenario: Receive incoming client request
    Given A client has made a request to the server
    When the request contains location data
    Then the server will generate requests to external APIs

Scenario: Use client location to generate sun location data
    Given the client has provided location data
    When a request has been received
    Then the server will generate map data and send a response

Scenario: Return data to client
    Given the client has provided data
    Then the server has generated a response
    And sent response back to client 
