from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from lesson12.pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """ Переход по ссылке """
        self.browser.get(self.url)

    def is_element_visible(self, locator, el_path):
        """ Проверка видимости элемента """
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((locator, el_path)),
            message=f'Cannot find element by locator {locator}, {el_path}')

    def is_title_correct(self, title):
        """ Проверка тайтла страницы """
        return WebDriverWait(self.browser, 5).until(
                EC.title_is(title), message="Wrong title")

    def is_element_clickable(self, locator, el_path):
        """ Проверка кликабельности элемента """
        return WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((locator, el_path)),
                message=f'Cannot find and click on element by locator {locator}, {el_path}')

    def select_products(self, locator, el_path):
        """ Создание класса Select """
        return Select(self.browser.find_element(locator, el_path))

    def search(self, txt):
        """ Поиск по сайту """
        self.__should_be_search_input()
        self.__should_be_search_button()
        self.__set_search_text(txt)
        self.__start_search()

    def __should_be_search_input(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*BasePageLocators.SEARCH_INPUT)

    def __should_be_search_button(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*BasePageLocators.SEARCH_BUTTON)

    def __set_search_text(self, txt):
        """ Ввод текста в поле поиска """
        self.is_element_visible(*BasePageLocators.SEARCH_INPUT).clear()
        self.is_element_visible(*BasePageLocators.SEARCH_INPUT).send_keys(txt)

    def __start_search(self):
        """ Нажатие на кнопку запуска поиска """
        self.is_element_visible(*BasePageLocators.SEARCH_BUTTON).click()
