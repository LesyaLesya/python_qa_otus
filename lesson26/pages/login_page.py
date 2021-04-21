from lesson26.pages.base_page import BasePage
from lesson26.pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_elements_on_page(self):
        """ Проверка видимости элементов на странице """
        self.__should_be_new_customer_form()
        self.__should_be_old_customer_form()
        self.__should_be_right_list_menu()
        self.__should_be_button_for_new_customer_form()
        self.__should_be_button_for_old_customer_form()

    def __should_be_new_customer_form(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*LoginPageLocators.NEW_CUSTOMER_FORM)

    def __should_be_old_customer_form(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*LoginPageLocators.OLD_CUSTOMER_FORM)

    def __should_be_right_list_menu(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*LoginPageLocators.RIGHT_LIST_MENU)

    def __should_be_button_for_new_customer_form(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*LoginPageLocators.BUTTON_FOR_NEW_CUSTOMER)

    def __should_be_button_for_old_customer_form(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*LoginPageLocators.BUTTON_FOR_OLD_CUSTOMER)
