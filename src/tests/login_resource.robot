*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Login Should Succeed
    Page Should Contain  Ohtu Application main page
Submit Login
    Click Button  Login

Login Should Fail With Message
    [Arguments]    ${message}
    Login Page Should Be Open
    Page Should Contain    ${message}