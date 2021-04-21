from lesson12.pages.base_page import BasePage
from lesson12.pages.locators import CataloguePageLocators


class CataloguePage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_elements_on_page(self):
        """ Проверка видимости элементов на странице """
        self.__should_be_breadcrumb()
        self.__should_be_header()
        self.__should_be_catalogue_image()
        self.__should_be_left_menu()
        self.__should_be_banner_under_left_menu()

    def compare(self):
        """ Добавление товара в сравнение """
        self.__should_be_product_in_catalogue()
        self.__add_to_compare()

    def should_be_successful_alert(self):
        """ Проверка отображения алерта после добавления товара в сравнение """
        assert self.is_element_visible(*CataloguePageLocators.ALERT_SUCCESS)

    def should_be_adding_in_compare_link(self, txt):
        """ Проверка изменения количества товаров в сравнении после добавления в сравнение """
        self.__should_be_compare_link()
        self.__get_text_after_adding_to_compare()
        assert self.__get_text_after_adding_to_compare() == txt

    def sort_by_name_a_z(self):
        """ Сортировка по имени от a до z """
        select = self.select_products(*CataloguePageLocators.SELECT_SORT)
        select.select_by_visible_text("Name (A - Z)")

    def get_first_product_after_sort(self, product):
        """ Проверка первого продукта после сортировки по имени от a до z """
        assert self.is_element_visible(*CataloguePageLocators.FIRST_PRODUCT_AFTER_SORT).text == product

    def get_last_product_after_sort(self, product):
        """ Проверка последнего продукта после сортировки по имени от a до z """
        assert self.is_element_visible(*CataloguePageLocators.LAST_PRODUCT_AFTER_SORT).text == product

    def __should_be_breadcrumb(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*CataloguePageLocators.BREADCRUMB)

    def __should_be_header(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*CataloguePageLocators.CATALOGUE_HEADER)

    def __should_be_catalogue_image(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*CataloguePageLocators.CATALOGUE_IMAGE)

    def __should_be_left_menu(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*CataloguePageLocators.LEFT_MENU)

    def __should_be_banner_under_left_menu(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*CataloguePageLocators.BANNER_UNDER_LEFT_MENU)

    def __should_be_product_in_catalogue(self):
        """ Проверка видимости первого товара странице """
        assert self.is_element_visible(*CataloguePageLocators.FIRST_PRODUCT)

    def __add_to_compare(self):
        """ Клик по кнопке добавления в сравнение """
        self.is_element_visible(*CataloguePageLocators.COMPARE_BUTTON).click()

    def __should_be_compare_link(self):
        """ Проверка видимости ссылки для перехода на страницу сравнения товаров """
        assert self.is_element_visible(*CataloguePageLocators.COMPARE_LINK)

    def __get_text_after_adding_to_compare(self):
        """ Получение текста из ссылки о количестве товаров в сравнении """
        return self.is_element_visible(*CataloguePageLocators.COMPARE_LINK).text
