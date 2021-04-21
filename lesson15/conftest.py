import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filemode='w',
    filename=f"lesson15/logs/selenium.log"
)


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default=None,
        help="Choose browser: chrome or firefox")
    parser.addoption(
        "--url",
        action="store",
        default="https://demo.opencart.com/",
        help="Enter url"
    )


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def browser(request):
    """ Запуск драйвера в зависимости от выбранного браузера """
    browser_name = request.config.getoption("browser_name")
    test_name = request.node.name
    module_name = request.module.__name__
    logger = logging.getLogger("BrowserLogger")
    logger.info(f"=== TESTING MODULE {module_name} ====")
    logger.info(f"Test '{test_name}' is starting")
    if browser_name == "chrome":
        options = webdriver.chrome.options.Options()
        options.headless = True
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        logger.info(f"Browser {browser_name} run")
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = webdriver.firefox.options.Options()
        options.headless = True
        browser = webdriver.Firefox(options=options)
        browser.maximize_window()
        logger.info(f"Browser {browser_name} run")
    else:
        logger.error("UsageError occured")
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
    logger.info(f"Browser {browser_name} closed")
    logger.info(f"Test '{test_name}' is finished\n\n")
