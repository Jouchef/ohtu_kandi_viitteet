*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5001
${DELAY}  1 seconds
${HOME_URL}  http://${SERVER}
${LOGIN_URL}  http://${SERVER}/login
${REGISTER_URL}  http://${SERVER}/register
${NEW_REFERENCE}  http://${SERVER}/form
${BROWSER}  chrome

*** Keywords ***
Open And Configure Browser
    # jos käytät Firefoxia ja Geckodriveriä käytä seuraavaa riviä sitä alemman sijaan
    # ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    # seuraava rivi on kommentoitu toistaiseksi pois
    # Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Page Should Contain Element  //h1[text()='Login']

Main Page Should Be Open
    Title Should Be  Reference app

New Reference Page Should Be Open
    Page Should Contain  Author

Go To Login Page
    Go To  ${LOGIN_URL}
Go To Register Page
    Go To  ${REGISTER_URL}

Go To Main Page
    Go To  ${HOME_URL}

Go To New Reference Page
    Go To  ${NEW_REFERENCE}


