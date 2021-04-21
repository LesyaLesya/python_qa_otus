from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    @allure.step("Открываем url {url}")
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """ Переход по ссылке """
        self.browser.get(self.url)

    @allure.step("Ищем элемент с локатором {locator} по пути {el_path}")
    def is_element_visible(self, locator, el_path):
        """ Проверка видимости элемента """
        try:
            return WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((locator, el_path)))
        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f'Cannot find element by locator {locator}, {el_path}')

    @allure.step("Проверяем корректность заголовка {title}")
    def is_title_correct(self, title):
        """ Проверка тайтла страницы """
        try:
            return WebDriverWait(self.browser, 5).until(
            EC.title_is(title))
        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Wrong title")

    @allure.step("Проверяем кликабельность элемента с локатором {locator} по пути {el_path}")
    def is_element_clickable(self, locator, el_path):
        """ Проверка кликабельности элемента """
        try:
            return WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((locator, el_path)))
        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f'Cannot find and click on element by locator {locator}, {el_path}')

    @allure.step("Получаем текст элемента с локатором {locator} по пути {el_path}")
    def get_text_of_element(self, locator, el_path):
        """ Получение текста элемента """
        try:
            el = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((locator, el_path)))
        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f'Cannot find element by locator {locator}, {el_path}')
        return el.text

    @allure.step("Кликаем по элементу с локатором {locator} по пути {el_path}")
    def click_on_element(self, locator, el_path):
        """ Клик по элементу """
        try:
            el = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((locator, el_path)))
        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f'Cannot find element by locator {locator}, {el_path}')
        return el.click()

    @allure.step("Очищаем инпут {el}")
    def clear_input(self, el):
        """ Очистка инпута """
        return el.clear()

    @allure.step("Вводим значение {key} в инпут {el}")
    def send_keys(self, el, key):
        """ Отправка значения в инпут """
        return el.send_keys(key)

    @allure.step("Ищем элемент с локатором {locator} по пути {el_path} и ищем по тексту {txt} ")
    def select_products(self, txt, locator, el_path):
        """ Создание класса Select """
        el = Select(self.browser.find_element(locator, el_path))
        return el.select_by_visible_text(txt)

    @allure.step("Получаем атрибут {attr} у элемента с локатором {locator} по пути {el_path}")
    def getting_attr(self, attr, locator, el_path):
        """ Получение атрибута элемента"""
        try:
            el = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located((locator, el_path)))
        except TimeoutException:
            allure.attach(
                body=self.browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f'Cannot find element by locator {locator}, {el_path}')
        return el.get_attribute(attr)
