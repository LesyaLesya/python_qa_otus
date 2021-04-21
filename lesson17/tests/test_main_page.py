from lesson17.pages.main_page import MainPage


def test_presence_of_elements_on_main_page(browser, url):
    """ Проверка присутствия элементов на странице """
    page = MainPage(browser, url)
    page.open()
    page.should_be_elements_on_page()


def test_is_main_page(browser, url):
    """ Проверка тайтла главной страницы """
    page = MainPage(browser, url)
    page.open()
    page.is_title_correct("Your Store")
