*** Settings ***
Documentation    Тесты для Open Cart на RobotFramework
Library    SeleniumLibrary
Resource    /lesson30_31/PageObject/MainPage.robot
Resource    /lesson30_31/PageObject/ProductPage.robot


Suite Setup    Open Browser    url=None    browser=${BROWSER}    remote_url=http://${REMOTE_EXECUTOR}:4444/wd/hub
Suite Teardown    Close Browser


*** Variables ***
${BROWSER}    chrome
${REMOTE_EXECUTOR}    localhost
${URL}    localhost


*** Test Cases ***
Test Visibility Of Elements On Main Page
    [Template]    Search for elements on main page
    ${BANNER}
    ${BANNER_PAGINATION_BULLETS}
    ${HEADER_FEATURED}
    ${CAROUSEL_BRAND}
    ${CAROUSEL_PAGINATION_BULLETS}


Test Get Title Of Main Page
    Go To    http://${URL}
    MainPage.Get Title Of Page    Your Store


Test Visibility Of Elements On Product Page
    [Template]    Search for elements on product page
    ${PRODUCT_HEADER}
    ${BUTTON_CART}
    ${IMAGES_BLOCK}
    ${RATING_BLOCK}
    ${PRODUCT_DESCRIPTION}


Test Open Product Image In Window By Click
    Go To    http://${URL}/index.php?route=product/product&path=18&product_id=47
    ProductPage.Check Click On Image    ${MAIN_PRODUCT_IMAGE}    ${PRODUCT_IMAGE_IN_WINDOW}


Test Click On Tabs In Product cart
    [Template]    Click On Tabs
    ${TAB_SPECIFICATION_LINK}    ${TAB_SPECIFICATION_CLASS}
    ${TAB_DESCRIPTION_LINK}    ${TAB_DESCRIPTION_CLASS}
    ${TAB_REVIEWS_LINK}    ${TAB_REVIEWS_CLASS}


*** Keywords ***
Search for elements on main page
    [Arguments]    ${selector}
    Go To    http://${URL}
    Wait Until Element Is Visible    ${selector}


Search for elements on product page
    [Arguments]    ${selector}
    Go To    http://${URL}/index.php?route=product/product&path=18&product_id=47
    Wait Until Element Is Visible    ${selector}


Click On Tabs
    [Arguments]    ${selector1}    ${selector2}
    Go To    http://${URL}/index.php?route=product/product&path=18&product_id=47
    Click Element   ${selector1}
    Wait Until Element Is Visible    ${selector2}
    ${ATTR}    Get Element Attribute    ${selector2}    class
    Should Be Equal    ${ATTR}    active
