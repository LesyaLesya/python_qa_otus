import allure
from lesson26.pages.admin_page import AdminPage


@allure.feature("Admin page")
@allure.story("Searching elements on Admin page")
@allure.title("Presence of elements on Admin page")
@allure.link("#", name="User story")
@allure.description("Проверка присутствия элементов на странице")
def test_presence_of_elements_on_admin_login_page(browser, url):
    """ Проверка присутствия элементов на странице """
    url = f'{url}admin/'
    page = AdminPage(browser, url)
    page.open()
    page.should_be_elements_on_page()


@allure.feature("Admin page")
@allure.story("Login to Admin page")
@allure.title("Valid credentials")
@allure.link("#", name="User story")
@allure.description("Проверка логина в админку с валидными креденшелами")
def test_login(browser, url):
    """ Проверка логина в админку с валидными креденшелами """
    url = f'{url}admin/'
    page = AdminPage(browser, url)
    page.open()
    page.login("demo", "demo")
    page.is_title_correct("Dashboard")


@allure.feature("Admin page")
@allure.story("Logout from Admin page")
@allure.title("Logout from Admin page by click on button")
@allure.link("#", name="User story")
@allure.description(" Проверка разлогина из админки")
def test_logout(browser, url):
    """ Проверка разлогина из админки """
    url = f'{url}admin/'
    page = AdminPage(browser, url)
    page.open()
    page.login("demo", "demo")
    page.logout()
    page.should_be_successful_logout_text()


@allure.feature("Admin page")
@allure.story("Getting product table")
@allure.title("Checking presence of product table")
@allure.link("#", name="User story")
@allure.description("Проверка отображения таблицы с товарами в админке")
def test_get_products_table(browser, url):
    """ Проверка отображения таблицы с товарами в админке """
    url = f'{url}admin/'
    page = AdminPage(browser, url)
    page.open()
    page.login("demo", "demo")
    page.get_product_table()
    page.should_be_table()
