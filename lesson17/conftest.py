import pytest
import logging
from selenium import webdriver


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filemode='w',
    filename=f"lesson17/logs/selenium.log"
)


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
        required=True,
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
        "name": test_name,
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": videos,
            "enableLog": logs
        }}

    logger = logging.getLogger("BrowserLogger")
    logger.info(f"=== TESTING MODULE {module_name} ====")
    logger.info(f"Test '{test_name}' is starting")
    browser = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                               desired_capabilities=caps)

    browser.maximize_window()
    logger.info(f"Browser {browser_name} run")
    yield browser
    browser.quit()
    logger.info(f"Browser {browser_name} closed")
    logger.info(f"Test '{test_name}' is finished\n\n")
