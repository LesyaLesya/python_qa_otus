from lesson15.pages.base_page import BasePage
from lesson15.pages.locators import HeaderPageLocators


class HeaderPage(BasePage):
    def search(self, txt):
        """ Поиск по сайту """
        self.__should_be_search_input()
        self.__should_be_search_button()
        self.__set_search_text(txt)
        self.__start_search()

    def __should_be_search_input(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*HeaderPageLocators.SEARCH_INPUT)

    def __should_be_search_button(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*HeaderPageLocators.SEARCH_BUTTON)

    def __set_search_text(self, txt):
        """ Ввод текста в поле поиска """
        search_input = self.is_element_visible(*HeaderPageLocators.SEARCH_INPUT)
        self.clear_input(search_input)
        self.send_keys(search_input, txt)

    def __start_search(self):
        """ Нажатие на кнопку запуска поиска """
        self.click_on_element(*HeaderPageLocators.SEARCH_BUTTON)
