*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  Testisalasana123!
    Set PasswordConfirmation  Testisalasana123!
    Submit New User
    User Creation Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  Testisalasana123!
    Set PasswordConfirmation  Testisalasana123!
    Submit New User
    User Creation Should Fail With  Username should be at least 3 characters long.

Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  kallekal
    Set PasswordConfirmation  kallekal
    Submit New User
    User Creation Should Fail With  The password should be 12 characters long and contain at least one uppercase letter, one number and one special character.

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  Testisalasana123!
    Set PasswordConfirmation  Testisalasana123
    Submit New User
    User Creation Should Fail With  Password and confirmation do not match.

Login After Successful Registration
    Set Username  kalle
    Set Password  Testisalasana123!
    Set PasswordConfirmation  Testisalasana123!
    Submit New User
    Go To Login Page
    Set Username  kalle
    Set Password  Testisalasana123!
    Submit Credentials
    Login Should Succeed

#Login After UnSuccessful Registration
#    Set Username  ka
#    Set Password  kalle123
#    Set PasswordConfirmation  kalle123
#    Submit New User
#    Go To Login Page
#    Set Username  ka
#    Set Password  kalle123
#    Submit Credentials
    #Login Should Fail With Message  Invalid username or password


*** Keywords ***
Submit New User
    Click Button  Register

User Creation Should Succeed
    Title Should Be  Reference app 

User Creation Should Fail With
    [Arguments]  ${expected_message}
    ${message} =    Handle Alert
    Should Be Equal  ${message}  ${expected_message}
    #Handle Alert    action=DISMISS
    #Alert Should Not Be Present
    



