from lesson12.pages.base_page import BasePage
from lesson12.pages.locators import AdminPageLocators


class AdminPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_elements_on_page(self):
        """ Проверка видимости элементов на странице """
        self.__should_be_panel_heading()
        self.__should_be_username_input()
        self.__should_be_password_input()
        self.__should_be_login_button()
        self.__should_be_help_block()

    def login(self, username, password):
        """ Ввод имени и пароля и нажатие на кнопку логина """
        self.__set_username(username)
        self.__set_password(password)
        self.__login_button_click()

    def logout(self):
        """ Нахождение кнопки разлогина и нажатие на нее """
        self.is_element_clickable(*AdminPageLocators.LOGOUT_BUTTON).click()

    def should_be_successful_logout_text(self):
        """ Проверка видимости элемента после разлогина """
        assert self.is_element_visible(*AdminPageLocators.NEED_LOGIN_TEXT)

    def get_product_table(self):
        """ Переход к таблице с товарами """
        self.__catalogue_click()
        self.__categories_click()

    def should_be_table(self):
        """ Проверка видимости таблицы """
        assert self.is_element_visible(*AdminPageLocators.CATEGORIES_TABLE)

    def __should_be_panel_heading(self):
        """ Проверка видимости элемента """
        assert self.is_element_visible(*AdminPageLocators.PANEL_HEADING)

    def __should_be_username_input(self):
        """ Проверка видимости элемента """
        assert self.is_element_visible(*AdminPageLocators.USERNAME_INPUT)

    def __should_be_password_input(self):
        """ Проверка видимости элемента """
        assert self.is_element_visible(*AdminPageLocators.PASSWORD_INPUT)

    def __should_be_login_button(self):
        """ Проверка видимости элемента """
        assert self.is_element_visible(*AdminPageLocators.LOGIN_BUTTON)

    def __should_be_help_block(self):
        """ Проверка видимости элемента """
        assert self.is_element_visible(*AdminPageLocators.HELP_BLOCK)

    def __set_username(self, name):
        """ Добавление имени в инпут """
        username = self.is_element_visible(*AdminPageLocators.USERNAME_INPUT)
        username.clear()
        username.send_keys(name)

    def __set_password(self, passw):
        """ Добавление пароля в инпут """
        password = self.is_element_visible(*AdminPageLocators.PASSWORD_INPUT)
        password.clear()
        password.send_keys(passw)

    def __login_button_click(self):
        """ Клик на кнопку логина """
        self.is_element_visible(*AdminPageLocators.LOGIN_BUTTON).click()

    def __catalogue_click(self):
        """ Клик по пункту Каталога """
        self.is_element_visible(*AdminPageLocators.LEFT_MENU_CATALOGUE).click()

    def __categories_click(self):
        """ Клик по пункту Категорий """
        self.is_element_visible(*AdminPageLocators.LEFT_MENU_CATEGORIES).click()
