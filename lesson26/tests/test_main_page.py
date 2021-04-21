import allure
from lesson26.pages.main_page import MainPage


@allure.feature("Main page")
@allure.story("Searching elements on Main page")
@allure.title("Presence of elements on Main page")
@allure.link("#", name="User story")
@allure.description("Проверка присутствия элементов на странице")
def test_presence_of_elements_on_main_page(browser, url):
    """ Проверка присутствия элементов на странице """
    page = MainPage(browser, url)
    page.open()
    page.should_be_elements_on_page()


@allure.feature("Main page")
@allure.story("Checking title of Main page")
@allure.title("Checking, that title is correct")
@allure.link("#", name="User story")
@allure.description("Проверка тайтла главной страницы")
def test_is_main_page(browser, url):
    """ Проверка тайтла главной страницы """
    page = MainPage(browser, url)
    page.open()
    page.is_title_correct("Your Store")
