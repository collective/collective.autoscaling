*** Variables ***

${TEST_FOLDER_ID} =  test-folder
${TEST_FOLDER} =  ${PLONE_URL}/${TEST_FOLDER_ID}


*** Keywords ***

# Settings

I am logged in as a ${role}
  Enable autologin as  ${role}
  Go to  ${PLONE_URL}

I go to the control panel
    Click link  css=#user-name
    Click link  link=Site Setup

I access collective.autoscaling settings
    Click link  link=Autoscaling
    Page Should Contain  Lets you change the settings of images autoscaling feature.

I choose to show message to user
    Select Checkbox  id=form-widgets-show_message-0
    Click Button  Save

I disabled autoscaling
    Unselect Checkbox  id=form-widgets-is_enabled-0
    Click Button  Save

I change settings to width '${setting_width}' and height '${setting_height}'
    Input text  id=form-widgets-image_max_width  ${setting_width}
    Input text  id=form-widgets-image_max_height  ${setting_height}
    Click Button  Save


# Content manipulation

I upload a big image called '${title}' in folder '${folder}'
    Go to  ${folder}
    Open Add New Menu
    Click Link  link=Image
    Wait Until Page Contains  Image
    Input text  name=form.widgets.title  ${title}
    Choose File  name=form.widgets.image  ${PATH_TO_TEST_FILES}/${title}
    Click Button  Save
    Wait Until Page Contains  Item created
    Page Should Contain  Item created

I create a content called '${title}' with two image fields using image '${image}'
    Go to  ${TEST_FOLDER}
    Open Add New Menu
    Click Link  link=dexterity content type with two image fields
    Input text  name=form.widgets.IDublinCore.title  ${title}
    Choose File  name=form.widgets.first_image  ${PATH_TO_TEST_FILES}/${image}
    Choose File  name=form.widgets.second_image  ${PATH_TO_TEST_FILES}/${image}
    Click Button  Save
    Wait Until Page Contains  Item created
    Page Should Contain  Item created

I delete the image '${content-id}'
    Delete image  ${TEST_FOLDER_ID}/${content-id}


# Checks

image '${content-id}' is scaled down to width '${setting_width}' and height '${setting_height}' and size '${size}'
    Go to  ${TEST_FOLDER}/${content-id}/view
    Page Should Contain  Size: ${size}
    ${size} =  image dimensions of  ${TEST_FOLDER_ID}/${content-id}
    ${width} =  Get From List  ${size}  0
    ${height} =  Get From List  ${size}  1
    Should Be Equal As Strings  ${width}  ${setting_width}
    Should Be Equal As Strings  ${height}  ${setting_height}

both images are scaled down for content '${title}' to width '${setting_width}' and height '${setting_height}'
    ${size} =  image dimensions of  ${TEST_FOLDER_ID}/${title}/first_image
    ${width} =  Get From List  ${size}  0
    ${height} =  Get From List  ${size}  1
    Should Be Equal As Strings  ${width}  ${setting_width}
    Should Be Equal As Strings  ${height}  ${setting_height}
    ${size} =  image dimensions of  ${TEST_FOLDER_ID}/${title}/second_image
    ${width} =  Get From List  ${size}  0
    ${height} =  Get From List  ${size}  1
    Should Be Equal As Strings  ${width}  ${setting_width}
    Should Be Equal As Strings  ${height}  ${setting_height}

information message for one image is shown
    Page Should Contain  One image was down sampled on this content.

information message for multiples images ('${nb}') is shown
    Page Should Contain  ${nb} images were down sampled on this content.

image '${content-id}' is not scaled down
    Go to  ${TEST_FOLDER}/${content-id}/view
    Page Should Contain  Size: 64KB


# View

I call resize-images view on '${path}'
    Go to  ${path}/@@resize-images

Nothing happens on '${path}'
    Page Should Contain  Scaling every images under folder ${path}.
    Page Should Contain  Nothing has to be done.

'${nb}' images were resized on '${path}'
    Page Should Contain  Scaling every images under folder ${path}.
    Page Should Contain  Finished to resize ${nb} images.
