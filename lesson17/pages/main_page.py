from lesson17.pages.base_page import BasePage
from lesson17.pages.locators import MainPageLocators


class MainPage(BasePage):
    def should_be_elements_on_page(self):
        """ Проверка видимости элементов на странице """
        self.__should_be_banner()
        self.__should_be_banner_pagination_bullets()
        self.__should_be_header_featured()
        self.__should_be_carousel_brand()
        self.__should_be_carousel_pagination_bullets()

    def __should_be_banner(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*MainPageLocators.BANNER)

    def __should_be_banner_pagination_bullets(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*MainPageLocators.BANNER_PAGINATION_BULLETS)

    def __should_be_header_featured(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*MainPageLocators.HEADER_FEATURED)

    def __should_be_carousel_brand(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*MainPageLocators.CAROUSEL_BRAND)

    def __should_be_carousel_pagination_bullets(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*MainPageLocators.CAROUSEL_PAGINATION_BULLETS)
