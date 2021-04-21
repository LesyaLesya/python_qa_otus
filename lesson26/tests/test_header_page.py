import pytest
import allure
from lesson26.pages.header_page import HeaderPage


@allure.feature("Header page")
@allure.story("Search by site")
@allure.title("Searching for {value}")
@allure.link("#", name="User story")
@allure.description("Проверка тайтла страницы с результатами поиска")
@pytest.mark.parametrize("value", ["phone", "laptop", "HP"], ids=["phone", "laptop", "HP"])
def test_search_result_title(browser, url, value):
    """ Проверка тайтла страницы с результатами поиска """
    page = HeaderPage(browser, url)
    page.open()
    page.search(value)
    page.is_title_correct(f"Search - {value}")
