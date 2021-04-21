from lesson12.pages.catalogue_page import CataloguePage


def test_presence_of_elements_on_catalogue_page(browser, url):
    """ Проверка присутствия элементов на странице """
    url = f'{url}index.php?route=product/category&path=18'
    page = CataloguePage(browser, url)
    page.open()
    page.should_be_elements_on_page()


def test_add_to_compare(browser, url):
    """ Проверка добавления товара в сравнение """
    url = f'{url}index.php?route=product/category&path=18'
    page = CataloguePage(browser, url)
    page.open()
    page.compare()
    page.should_be_successful_alert()
    page.should_be_adding_in_compare_link("Product Compare (1)")



def test_sort_by_name_a_z(browser, url):
    """ Проверка работы сортировки по имени от a до z """
    url = f'{url}index.php?route=product/category&path=18'
    page = CataloguePage(browser, url)
    page.open()
    page.sort_by_name_a_z()
    page.get_first_product_after_sort("HP LP3065")
    page.get_last_product_after_sort("Sony VAIO")
