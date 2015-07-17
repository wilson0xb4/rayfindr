Feature: Rayfindr API
    An API that returns shadow projections based on time/location.

Scenario:
    Given I am a client with a time and location
    When I send an AJAX POST request
    Then I should recieve a JSON response with shadow data
    And the shadow data should match my time and location
