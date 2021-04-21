from lesson12.pages.admin_page import AdminPage


def test_presence_of_elements_on_admin_login_page(browser, url):
    """ Проверка присутствия элементов на странице """
    url = f'{url}admin/'
    page = AdminPage(browser, url)
    page.open()
    page.should_be_elements_on_page()


def test_login(browser, url):
    """ Проверка логина в админку с валидными креденшелами """
    url = f'{url}admin/'
    page = AdminPage(browser, url)
    page.open()
    page.login("user", "bitnami")
    page.is_title_correct("Dashboard")


def test_logout(browser, url):
    """ Проверка разлогина из админки """
    url = f'{url}admin/'
    page = AdminPage(browser, url)
    page.open()
    page.login("user", "bitnami")
    page.logout()
    page.should_be_successful_logout_text()


def test_get_products_table(browser, url):
    """ Проверка отображения таблицы с товарами в админке """
    url = f'{url}admin/'
    page = AdminPage(browser, url)
    page.open()
    page.login("user", "bitnami")
    page.get_product_table()
    page.should_be_table()
