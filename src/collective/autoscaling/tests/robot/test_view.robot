*** Settings ***

Resource        plone/app/robotframework/selenium.robot
Resource        plone/app/robotframework/keywords.robot
Resource        collective/autoscaling/tests/robot/keywords.robot

Library         Collections
Library         Remote  ${PLONE_URL}/RobotRemote
Variables       plone/app/testing/interfaces.py
Variables       collective/autoscaling/tests/variables.py

Test Setup      Open test browser
Test Teardown   Close all browsers


*** Test Cases ***

Scenario: When I call resize-images view on an empty folder, nothing happens
  Given I am logged in as a Manager
   When I call resize-images view on '${TEST_FOLDER}'
   Then Nothing happens on '${TEST_FOLDER}'

Scenario: When I call resize-images view on a folder, all images are rescaled
  Given I am logged in as a Manager
   When I go to the control panel
    And I access collective.autoscaling settings
    And I disabled autoscaling
   When I upload a big image called 'big-image.png' in folder '${TEST_FOLDER}'
    And I upload a big image called 'big-image.png' in folder '${TEST_FOLDER}'
    And I upload a big image called 'big-image.png' in folder '${TEST_FOLDER}'
    And I upload a big image called 'big-image.png' in folder '${TEST_FOLDER}'
   When I call resize-images view on '${TEST_FOLDER}'
   Then '4' images were resized on '${TEST_FOLDER}'

Scenario: When I call resize-images view on the Plone site, all images are rescaled
  Given I am logged in as a Manager
   When I go to the control panel
    And I access collective.autoscaling settings
    And I disabled autoscaling
   When I upload a big image called 'big-image.png' in folder '${TEST_FOLDER}'
    And I upload a big image called 'big-image.png' in folder '${PLONE_URL}'
   When I call resize-images view on '${PLONE_URL}'
   Then '2' images were resized on '${PLONE_URL}'
