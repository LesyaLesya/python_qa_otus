from lesson17.pages.login_page import LoginPage


def test_presence_of_elements_on_login_page(browser, url):
    """ Проверка присутствия элементов на странице """
    url = f'{url}index.php?route=account/login'
    page = LoginPage(browser, url)
    page.open()
    page.should_be_elements_on_page()
