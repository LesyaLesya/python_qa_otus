import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


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
        browser = webdriver.Firefox(options=options)
        browser.maximize_window()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
