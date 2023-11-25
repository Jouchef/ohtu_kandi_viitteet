*** Settings ***
Library  SeleniumLibrary
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  heksaani
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  he
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Invalid Password
    Set Username  heksaani
    Set Password  salasana
    Set Password Confirmation  salasana
    Submit Registration
    Register Should Fail With Message  Password must contain numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  heksaani
    Set Password  salasana123
    Set Password Confirmation  salasana
    Submit Registration
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Set Username  heksaani
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration
    Go To Login Page
    Set Username  heksaani
    Set Password  salasana123
    Submit Login
    Login Should Succeed
    
Login After Failed Registration
    Set Username  heksaani
    Set Password  salasana1234
    Set Password Confirmation  salasana
    Submit Registration
    Go To Login Page
    Set Username  heksaani
    Set Password  salasana1234
    Submit Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Submit Registration
    Click Button  Register

Register Should Succeed
   Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}