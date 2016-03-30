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

Scenario: As a site administrator I can access Autoscaling settings
  Given I am logged in as a Manager
   When I go to the control panel
   Then I access collective.autoscaling settings
