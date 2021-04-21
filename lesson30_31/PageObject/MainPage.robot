*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${BANNER}    css=#content .swiper-viewport:nth-child(1)
${BANNER_PAGINATION_BULLETS}    css=.swiper-pagination.slideshow0.swiper-pagination-clickable.swiper-pagination-bullets
${HEADER_FEATURED}    tag=h3
${CAROUSEL_BRAND}    css=#carousel0.swiper-container-horizontal
${CAROUSEL_PAGINATION_BULLETS}    css=.swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets


*** Keywords ***
Get title of page
    [Arguments]    ${value}
    ${TITLE}    Get Title
    Should Be Equal    ${TITLE}    ${value}
