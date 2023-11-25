*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py


*** Variables ***
${SERVER}          localhost:5001
${DELAY}           3
${HOME_URL}        http://${SERVER}
#${LOGIN_URL}       http://${SERVER}/login
#${REGISTER_URL}    http://${SERVER}/register
#${NEW_REFERENCE}   http://${SERVER}/new_reference
#${EDIT_REFERENCE}  http://${SERVER}/edit_reference


*** Keywords ***
Open And Configure Browser
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    #Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Index Page Should Be Open
    Location Should Be  ${HOME_URL}
Go To Login Page
    Go To  ${LOGIN_URL}
Go To Register Page
    Go To  ${REGISTER_URL}
Go To New Reference Page
    Go To  ${NEW_REFERENCE}


