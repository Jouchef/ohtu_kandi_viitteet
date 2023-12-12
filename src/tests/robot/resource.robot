*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0.2 seconds
${HOME_URL}  http://127.0.0.1:5000
${LOGIN_URL}  ${HOME_URL}/login
${REGISTER_URL}  ${HOME_URL}/register
${NEW_REFERENCE}  ${HOME_URL}/new_reference

*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    #Call Method  ${options}  add_argument  --headless
    Reset Application
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Page Should Contain Element  //h1[text()='Login']

Main Page Should Be Open
    Title Should Be  Reference app

New Reference Page Should Be Open
    Page Should Contain  Type 

Register Page Should Be Open
    Page Should Contain Element  //h1[text()='Register']

Login Should Succeed
    Main Page Should Be Open
Go To Login Page
    Go To  ${LOGIN_URL}
Go To Register Page
    Go To  ${REGISTER_URL}

Go To Main Page
    Go To  ${HOME_URL}

Go To New Reference Page
    Go To  ${NEW_REFERENCE}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set PasswordConfirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Login

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Login Page
    Create User  kalle  Testisalasana123!
    Go To Login Page
    Login Page Should Be Open
Delete Test Setup
    Create User And Go To Login Page
    Set Username  kalle
    Set Password  Testisalasana123!
    Submit Credentials
    Main Page Should Be Open
    Click Link  Add
    New Reference Page Should Be Open
    