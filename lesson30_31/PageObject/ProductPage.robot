*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${PRODUCT_HEADER}    css=.btn-group + h1
${BUTTON_CART}    id=button-cart
${IMAGES_BLOCK}    class=thumbnails
${RATING_BLOCK}    class=rating
${PRODUCT_DESCRIPTION}    css=#tab-description > p
${MAIN_PRODUCT_IMAGE}    xpath=//ul[@class="thumbnails"]/li[1]
${PRODUCT_IMAGE_IN_WINDOW}    css=.mfp-figure
${TAB_DESCRIPTION_CLASS}    xpath=//ul[@class="nav nav-tabs"]/li[1]
${TAB_SPECIFICATION_CLASS}    xpath=//ul[@class="nav nav-tabs"]/li[2]
${TAB_REVIEWS_CLASS}    xpath=//ul[@class="nav nav-tabs"]/li[3]
${TAB_DESCRIPTION_LINK}    xpath=//a[@href="#tab-description"]
${TAB_SPECIFICATION_LINK}    xpath=//a[@href="#tab-specification"]
${TAB_REVIEWS_LINK}    xpath=//a[@href="#tab-review"]


*** Keywords ***
Check click on image
    [Arguments]    ${selector1}    ${selector2}
    Click Element    ${selector1}
    Wait Until Element Is Visible    ${selector2}
