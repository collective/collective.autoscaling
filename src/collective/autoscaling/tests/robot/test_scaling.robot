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
   When I upload a big image called 'big-image.png'
   Then image 'big-image.png' is scaled down   
    And I delete the image 'big-image.png'

Scenario: I see an information message if it is activated in settings
  Given I am logged in as a Manager
   When I go to the control panel
    And I access collective.autoscaling settings
    And I choose to show message to user
    And I upload a big image called 'big-image.png'
   Then information message is shown
    And I delete the image 'big-image.png'

Scenario: If the addon is not enabled, no image are scaled down automatically
  Given I am logged in as a Manager
   When I go to the control panel
    And I access collective.autoscaling settings
    And I disabled autoscaling
    And I upload a big image called 'big-image.png'
   Then image 'big-image.png' is not scaled down   
    And I delete the image 'big-image.png'
