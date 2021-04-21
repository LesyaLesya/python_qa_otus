from lesson17.pages.product_page import ProductPage


def test_presence_of_elements_on_product_page(browser, url):
    """ Проверка присутствия элементов на странице """
    url = f'{url}index.php?route=product/product&path=18&product_id=47'
    page = ProductPage(browser, url)
    page.open()
    page.should_be_elements_on_page()


def test_open_image_in_window_by_click(browser, url):
    """ Проверка открытия картинку во всплывающем окне по клику """
    url = f'{url}index.php?route=product/product&path=18&product_id=47'
    page = ProductPage(browser, url)
    page.open()
    page.click_main_product_image()
    page.get_main_image_in_window()


def test_click_on_tabs(browser, url):
    """ Проверка перехода по табам """
    url = f'{url}index.php?route=product/product&path=18&product_id=47'
    page = ProductPage(browser, url)
    page.open()
    page.click_on_tabs()
