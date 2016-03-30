*** Variables ***

${TEST_FOLDER_ID} =  test-folder
${TEST_FOLDER} =  ${PLONE_URL}/${TEST_FOLDER_ID}


*** Keywords ***

I am logged in as a ${role}
  Enable autologin as  ${role}
  Go to  ${PLONE_URL}

I go to the control panel
    Click link  css=#user-name
    Click link  link=Site Setup

I access collective.autoscaling settings
    Click link  link=Autoscaling
    Page Should Contain  Lets you change the settings of images autoscaling feature.

I upload a big image called '${title}'
    Go to  ${TEST_FOLDER}
    Open Add New Menu
    Click Link  link=Image
    Wait Until Page Contains  Image
    Input text  name=form.widgets.title  ${title}
    Choose File  name=form.widgets.image  ${PATH_TO_TEST_FILES}/${title}
    Click Button  Save
    Wait Until Page Contains  Item created
    Page Should Contain  Item created

image '${content-id}' is scaled down
    Go to  ${TEST_FOLDER}/${content-id}/view
    Page Should Contain  Size: 47KB
    ${size} =  image dimensions of  ${TEST_FOLDER_ID}/${content-id}
    ${width} =  Get From List  ${size}  0
    ${height} =  Get From List  ${size}  1
    Should Be Equal As Strings  ${width}  1200
    Should Be Equal As Strings  ${height}  600

I choose to show message to user
    Select Checkbox  id=form.show_message
    Click Button  Save

information message is shown
    Page Should Contain  One image has been resized on this content.

I disabled autoscaling
    Unselect Checkbox  id=form.is_enabled
    Click Button  Save

image '${content-id}' is not scaled down
    Go to  ${TEST_FOLDER}/${content-id}/view
    Page Should Contain  Size: 64KB

I delete the image '${content-id}'
    Delete image  ${TEST_FOLDER_ID}/${content-id}
