# rayfindr
API to find the sunny parts of an area?

## Build Status
master: [rayfindr.com](http://rayfindr.com) [![Build Status](https://travis-ci.org/wilson0xb4/rayfindr.svg?branch=master)](https://travis-ci.org/wilson0xb4/rayfindr)  
staging: [dev.rayfindr.com](http://dev.rayfindr.com) [![Build Status](https://travis-ci.org/wilson0xb4/rayfindr.svg?branch=staging)](https://travis-ci.org/wilson0xb4/rayfindr)

## Deployment
[Instructions and config files](https://github.com/wilson0xb4/rayfindr-config)

## Plans
1. Setup: Repo, AWS, Milestones / Issues, Tests (Travis)
2. App Framework (Flask)
3. Folders / Files
4. API's (GET)
  - Google (map overlay, building info)
  - Sun calculations or JS
  - Forcast.io (weather)
5. UI: Simple
6. API's (POST)

## User Stories
#### Developer
1. As a Developer I want to be able to deploy easily.
2. As a Developer I want to quickly see that my build is operational and passing tests.
3. As a Developer I want to allow others to utilize my API for gathering data and creating unique Client interfaces.

#### User
1. As a User I want to be able to navigate to the website, and quickly locate myself on a map showing available areas of sun.
2. As a User I want to see the most current (real-time) weather data overlaid on my map.

## Milestones
### Pre
- Deployment
- Testing
- HelloWorld!
- Choose API's

### Monday
- Architechture
- Client
  - map and basic overlay
- Tests

### Tuesday
- First pass implementation
- Client
  - map and overlay get smarter!

### Wednesday
Provisional Launch?

### Thursday
- bugfix/
- stretch goals

### Friday
Final Presentation! 

## Git Workflow
- master
  - staging
    - feature1
      - personal
    - feature2

master: deployable  
staging: final testing before deploying  
feature: pull request into staging?  
personal: when finished with issue or feature, do pull request into feature  
