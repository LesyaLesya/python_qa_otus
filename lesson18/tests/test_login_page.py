from lesson18.pages.login_page import LoginPage
import allure


@allure.feature("Login page")
@allure.story("Searching elements on Login page")
@allure.title("Presence of elements on Login page")
@allure.link("#", name="User story")
@allure.description("Проверка присутствия элементов на странице")
def test_presence_of_elements_on_login_page(browser, url):
    """ Проверка присутствия элементов на странице """
    url = f'{url}index.php?route=account/login'
    page = LoginPage(browser, url)
    page.open()
    page.should_be_elements_on_page()
