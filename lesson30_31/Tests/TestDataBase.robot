*** Settings ***
Library    String

Resource  /lesson30_31/PageObject/AdminPage.robot
Resource  /lesson30_31/Resources/DataBase.robot

Suite Setup  Connect To Database  pymysql  ${DBName}  ${DBUser}  ${DBPass}  ${DBHost}  ${DBPort}
Suite Teardown  Disconnect From Database

Test Setup  Open Browser    url=None    browser=${BROWSER}    remote_url=http://${REMOTE_EXECUTOR}:4444/wd/hub
Test Teardown  Close Browser


*** Variables ***
${BROWSER}    chrome
${REMOTE_EXECUTOR}    localhost
${URL}    localhost
${DBName}    bitnami_opencart
${DBUser}    bn_opencart
${DBPass}
${DBHost}    127.0.0.1
${DBPort}    3306
${URL}    localhost
@{USER_DATA} =    Alena    TEST    test111@test111.ru    12345677    qwe123!


*** Test Cases ***
Add User To Db
    [Documentation]    Регистрация нового пользователя с проверкой его добавления в БД
    [Teardown]    Run Keywords    Execute Sql String    delete from ${CUSTOMER_DB} where firstname = '${USER_DATA}[0]' and lastname = '${USER_DATA}[1]'
    ...  AND  Close Browser
    Go To    http://${URL}
    AdminPage.Go To Register Form
    AdminPage.Register New User    ${USER_DATA}
    Wait Until Keyword Succeeds    3 sec    1 sec    Check User In Database    ${USER_DATA}
