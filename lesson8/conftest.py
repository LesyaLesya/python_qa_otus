import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = webdriver.chrome.options.Options()
        options.headless = True
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        options = webdriver.firefox.options.Options()
        options.headless = True
        options.add_argument("headless")
        browser = webdriver.Firefox(options=options)
        browser.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestClassFindEl:
    def find_visible_element(self, browser, loc, el_path, message):
        try:
            el = WebDriverWait(browser, 5).until(
                EC.visibility_of_element_located(
                    (loc, el_path)))
        except TimeoutException:
            assert False, message
        return el

    def assert_title(self, browser, title, message):
        try:
            t = WebDriverWait(browser, 5).until(
                EC.title_is(title))
        except TimeoutException:
            assert False, message
        return t

    def wait_clickable_el(self, browser, loc, el_path, message):
        try:
            el = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((loc, el_path)))
        except TimeoutException:
            assert False, message
        return el


@pytest.fixture()
def fixture_find_element():
    return TestClassFindEl()
