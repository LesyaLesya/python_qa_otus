import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.logger = logging.getLogger(type(self).__name__)

    def open(self):
        """ Переход по ссылке """
        self.logger.info(f"Opening url {self.url}")
        self.browser.get(self.url)

    def is_element_visible(self, locator, el_path):
        """ Проверка видимости элемента """
        self.logger.info(f"Checking visibility of element with locator {locator} - {el_path}")
        return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((locator, el_path)),
            message=f'Cannot find element by locator {locator}, {el_path}')

    def is_title_correct(self, title):
        """ Проверка тайтла страницы """
        self.logger.info(f"Checking title '{title}' of page")
        return WebDriverWait(self.browser, 5).until(
                EC.title_is(title), message="Wrong title")

    def is_element_clickable(self, locator, el_path):
        """ Проверка кликабельности элемента """
        self.logger.info(f"Checking clickability of element with locator {locator} - {el_path}")
        return WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((locator, el_path)),
                message=f'Cannot find and click on element by locator {locator}, {el_path}')

    def get_text_of_element(self, locator, el_path):
        """ Получение текста элемента """
        self.logger.info(f"Getting text of element with locator {locator} - {el_path}")
        el = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located((locator, el_path)),
                message=f'Cannot find element by locator {locator}, {el_path}')
        return el.text

    def click_on_element(self, locator, el_path):
        """ Клик по элементу """
        self.logger.info(f"Clicking on element with locator {locator} - {el_path}")
        el = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located((locator, el_path)),
                message=f'Cannot find element by locator {locator}, {el_path}')
        return el.click()

    def clear_input(self, el):
        """ Очистка инпута """
        self.logger.info(f"Clearing input of element {el}")
        return el.clear()

    def send_keys(self, el, key):
        """ Отправка значения в инпут """
        self.logger.info(f"Send text '{key}' to element {el}")
        return el.send_keys(key)

    def select_products(self, txt, locator, el_path):
        """ Создание класса Select """
        self.logger.info(f"Finding select input by locator {locator} - {el_path} and select by text '{txt}'")
        el = Select(self.browser.find_element(locator, el_path))
        return el.select_by_visible_text(txt)

    def getting_attr(self, attr, locator, el_path):
        """ Получение атрибута элемента"""
        self.logger.info(f"Finding input by locator {locator} - {el_path} and getting attribute '{attr}'")
        el = WebDriverWait(self.browser, 5).until(
                EC.visibility_of_element_located((locator, el_path)),
                message=f'Cannot find element by locator {locator}, {el_path}')
        return el.get_attribute(attr)
