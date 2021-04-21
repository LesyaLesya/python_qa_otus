import allure
from lesson26.pages.product_page import ProductPage


@allure.feature("Product page")
@allure.story("Searching elements on Product page")
@allure.title("Presence of elements on Product page")
@allure.link("#", name="User story")
@allure.description("Проверка присутствия элементов на странице")
def test_presence_of_elements_on_product_page(browser, url):
    """ Проверка присутствия элементов на странице """
    url = f'{url}index.php?route=product/product&path=18&product_id=47'
    page = ProductPage(browser, url)
    page.open()
    page.should_be_elements_on_page()


@allure.feature("Product page")
@allure.story("Checking main image")
@allure.title("Checking opening main image by click")
@allure.link("#", name="User story")
@allure.description("Проверка открытия картинку во всплывающем окне по клику")
def test_open_image_in_window_by_click(browser, url):
    """ Проверка открытия картинку во всплывающем окне по клику """
    url = f'{url}index.php?route=product/product&path=18&product_id=47'
    page = ProductPage(browser, url)
    page.open()
    page.click_main_product_image()
    page.get_main_image_in_window()


@allure.feature("Product page")
@allure.story("Checking tabs")
@allure.title("Checking tabs is active after click")
@allure.link("#", name="User story")
@allure.description("Проверка перехода по табам")
def test_click_on_tabs(browser, url):
    """ Проверка перехода по табам """
    url = f'{url}index.php?route=product/product&path=18&product_id=47'
    page = ProductPage(browser, url)
    page.open()
    page.click_on_tabs()
