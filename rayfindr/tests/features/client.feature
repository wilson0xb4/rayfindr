Feature: Client
    Request mapping data to render sunny locations in real time.


Scenario: Generate and Send location data to server
    Given The user opens the client web page
    And the client allows location tracking
    Then the browser sends a location data package to the server

Scenario: Receive sun location from server
    Given a location data package has been sent to the server
    When the user opens the client web page
    Then the client receives a data package from the server
    And updates the client map software with Sun location data points
