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

Scenario: When I upload an image it is scaled down automatically
  Given I am logged in as a Manager
   When I upload a big image called 'big-image.png' in folder '${TEST_FOLDER}'
   Then image 'big-image.png' is scaled down to width '1200' and height '600' and size '47KB'
    And I delete the image 'big-image.png'

Scenario: I see an information message if it is activated in settings
  Given I am logged in as a Manager
   When I go to the control panel
    And I access collective.autoscaling settings
    And I choose to show message to user
    And I upload a big image called 'big-image.png' in folder '${TEST_FOLDER}'
   Then information message for one image is shown
    And I delete the image 'big-image.png'

Scenario: When I upload images on fields they are scaled down automatically
  Given I am logged in as a Manager
   When I go to the control panel
    And I access collective.autoscaling settings
    And I choose to show message to user
   When I create a content called 'doc' with two image fields using image 'big-image.png'
   Then both images are scaled down for content 'doc' to width '1200' and height '600'
    And information message for multiples images ('2') is shown

Scenario: When I upload an image it is scaled down to new settings
  Given I am logged in as a Manager
   When I go to the control panel
    And I access collective.autoscaling settings
    And I change settings to width '400' and height '800'
    And I upload a big image called 'big-image.png' in folder '${TEST_FOLDER}'
   Then image 'big-image.png' is scaled down to width '400' and height '200' and size '14KB'
    And I delete the image 'big-image.png'

Scenario: If the addon is not enabled, no image are scaled down automatically
  Given I am logged in as a Manager
   When I go to the control panel
    And I access collective.autoscaling settings
    And I disabled autoscaling
    And I upload a big image called 'big-image.png' in folder '${TEST_FOLDER}'
   Then image 'big-image.png' is not scaled down
    And I delete the image 'big-image.png'
