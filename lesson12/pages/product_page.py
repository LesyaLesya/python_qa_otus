from lesson12.pages.base_page import BasePage
from lesson12.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_elements_on_page(self):
        """ Проверка видимости элементов на странице """
        self.__should_be_product_header()
        self.__should_be_button_cart()
        self.__should_be_images_block()
        self.__should_be_rating_block()
        self.__should_be_product_description()

    def click_on_tabs(self):
        """ Клики по табам и проверки активации табов """
        self.__click_on_tab_specification()
        self.__click_on_tab_reviews()
        self.__click_on_tab_description()

    def click_main_product_image(self):
        """ Клик по главной картинке """
        self.is_element_visible(*ProductPageLocators.MAIN_PRODUCT_IMAGE).click()

    def get_main_image_in_window(self):
        """ Проверка, что картинка открывается в окне по клику """
        assert self.is_element_visible(*ProductPageLocators.PRODUCT_IMAGE_IN_WINDOW)

    def __should_be_product_header(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*ProductPageLocators.PRODUCT_HEADER)

    def __should_be_button_cart(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*ProductPageLocators.BUTTON_CART)

    def __should_be_images_block(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*ProductPageLocators.IMAGES_BLOCK)

    def __should_be_rating_block(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*ProductPageLocators.RATING_BLOCK)

    def __should_be_product_description(self):
        """ Проверка видимости элемента на странице """
        assert self.is_element_visible(*ProductPageLocators.PRODUCT_DESCRIPTION)

    def __click_on_tab_specification(self):
        """ Клик по табу Specification """
        self.is_element_visible(*ProductPageLocators.TAB_SPECIFICATION_LINK).click()
        assert self.is_element_visible(*ProductPageLocators.TAB_SPECIFICATION_CLASS).get_attribute("class") == "active"

    def __click_on_tab_reviews(self):
        """ Клик по табу Reviews """
        self.is_element_visible(*ProductPageLocators.TAB_REVIEWS_LINK).click()
        assert self.is_element_visible(*ProductPageLocators.TAB_REVIEWS_CLASS).get_attribute("class") == "active"

    def __click_on_tab_description(self):
        """ Клик по табу Description """
        self.is_element_visible(*ProductPageLocators.TAB_DESCRIPTION_LINK).click()
        assert self.is_element_visible(*ProductPageLocators.TAB_DESCRIPTION_CLASS).get_attribute("class") == "active"
