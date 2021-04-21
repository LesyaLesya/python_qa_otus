import pytest
import allure
import json
import requests
import time
from selenium import webdriver


@allure.step("Waiting for resource availability {url}")
def url_data(url, timeout=10):
    while timeout:
        response = requests.get(url)
        if not response.ok:
            time.sleep(1)
            timeout -= 1
        else:
            if 'video' in url:
                return response.content
            else:
                return response.text
    return None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox")
    parser.addoption(
        "--url",
        action="store",
        default="https://demo.opencart.com/",
        help="Enter url")
    parser.addoption(
        "--executor",
        action="store",
        default="127.0.0.1",
        help="Enter your host")
    parser.addoption(
        "--browserVersion",
        action="store",
        default="87.0",
        help="Enter browser version")
    parser.addoption(
        "--vnc",
        action="store_true",
        default=False,
        help="Choose True or False for option")
    parser.addoption(
        "--logs",
        action="store_true",
        default=False,
        help="Choose True or False for option")
    parser.addoption(
        "--videos",
        action="store_true",
        default=False,
        help="Choose True or False for option")


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def browser(request):
    """ Запуск драйвера в зависимости от выбранного браузера """
    browser_name = request.config.getoption("--browser_name")
    executor = request.config.getoption("--executor")
    bversion = request.config.getoption("--browserVersion")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    test_name = request.node.name
    module_name = request.module.__name__

    caps = {
        "browserName": browser_name,
        "browserVersion": bversion,
        "screenResolution": "1440x900",
        "name": test_name + module_name,
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": videos,
            "enableLog": logs
        }}

    browser = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                               desired_capabilities=caps)

    # Attach browser data
    allure.attach(
        name=browser.session_id,
        body=json.dumps(browser.desired_capabilities),
        attachment_type=allure.attachment_type.JSON)

    # Add environment info to allure-report
    with open("allure-report/environment.xml", "w+") as file:
        file.write(f"""<environment>
            <parameter>
                <key>Browser</key>
                <value>{browser_name}</value>
            </parameter>
            <parameter>
                <key>Browser.Version</key>
                <value>{bversion}</value>
            </parameter>
            <parameter>
                <key>Executor</key>
                <value>http://{executor}:4444/wd/hub"</value>
            </parameter>
        </environment>
        """)

    browser.maximize_window()
    yield browser
    browser.quit()
    if request.node.status != 'passed':
        if logs:
            allure.attach(
                name="selenoid_log_" + browser.session_id,
                body=url_data(f"{executor}/logs/{browser.session_id}.log"),
                attachment_type=allure.attachment_type.TEXT)
        if videos:
            allure.attach(
                body=url_data(f"http://{executor}:8080/video/{browser.session_id}.mp4"),
                name="video_for_" + browser.session_id,
                attachment_type=allure.attachment_type.MP4)

    if videos and url_data(f"http://{executor}:8080/video/{browser.session_id}.mp4"):
        requests.delete(url=f"http://{executor}:8080/video/{browser.session_id}.mp4")
    if logs and url_data(f"{executor}/logs/{browser.session_id}.log"):
        requests.delete(url=f"{executor}/logs/{browser.session_id}.log")
