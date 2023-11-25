*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser


*** Test Cases ***
Click Home Link
    Go To  Home Page
    Home Page Should Be Open
#*** Keywords ***
#Submit Citation
    Click Button  Submit

#Set Author
#    [Arguments]  ${author}
#    Input Text  id=author  ${author}

#Set Title
 #   [Arguments]  ${title}
  #  Input Text  id=title  ${title}

#Set Journal
#    [Arguments]  ${journal}
#    Input Text  id=journal  ${journal}

#Set Year
#    [Arguments]  ${year}
#    Input Text  id=year  ${year}

#Set Volume
#    [Arguments]  ${volume}
#    Input Text  id=volume  ${volume}

#Set Pages
#    [Arguments]  ${pages}
#    Input Text  id=pages  ${pages}

#Set Publisher
#    [Arguments]  ${publisher}
#    Input Text  id=publisher  ${publisher}

