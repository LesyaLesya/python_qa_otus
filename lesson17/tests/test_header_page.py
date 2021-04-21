import pytest
from lesson17.pages.header_page import HeaderPage


@pytest.mark.parametrize("value", ["phone", "laptop", "HP"])
def test_search_result_title(browser, url, value):
    """ Проверка тайтла страницы с результатами поиска """
    page = HeaderPage(browser, url)
    page.open()
    page.search(value)
    page.is_title_correct(f"Search - {value}")
