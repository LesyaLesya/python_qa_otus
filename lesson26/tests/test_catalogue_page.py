import allure
from lesson26.pages.catalogue_page import CataloguePage


@allure.feature("Catalogue page")
@allure.story("Searching elements on Catalogue page")
@allure.title("Presence of elements on Catalogue page")
@allure.link("#", name="User story")
@allure.description("Проверка присутствия элементов на странице")
def test_presence_of_elements_on_catalogue_page(browser, url):
    """ Проверка присутствия элементов на странице """
    url = f'{url}index.php?route=product/category&path=18'
    page = CataloguePage(browser, url)
    page.open()
    page.should_be_elements_on_page()


@allure.feature("Catalogue page")
@allure.story("Adding product to compare list")
@allure.title("Checking product was added to compare list")
@allure.link("#", name="User story")
@allure.description("Проверка добавления товара в сравнение")
def test_add_to_compare(browser, url):
    """ Проверка добавления товара в сравнение """
    url = f'{url}index.php?route=product/category&path=18'
    page = CataloguePage(browser, url)
    page.open()
    page.compare()
    page.should_be_successful_alert()
    page.should_be_adding_in_compare_link("Product Compare (1)")


@allure.feature("Catalogue page")
@allure.story("Sorting products")
@allure.title("Sorting products by name from A to Z")
@allure.link("#", name="User story")
@allure.description("Проверка работы сортировки по имени от a до z")
def test_sort_by_name_a_z(browser, url):
    """ Проверка работы сортировки по имени от a до z """
    url = f'{url}index.php?route=product/category&path=18'
    page = CataloguePage(browser, url)
    page.open()
    page.sort_by_name_a_z()
    page.get_first_product_after_sort("HP LP3065")
    page.get_last_product_after_sort("Sony VAIO")
