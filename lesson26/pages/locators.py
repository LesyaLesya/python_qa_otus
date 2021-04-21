from selenium.webdriver.common.by import By


class HeaderPageLocators:
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".btn.btn-default.btn-lg")


class MainPageLocators:
    BANNER = (By.CSS_SELECTOR, "#content .swiper-viewport:nth-child(1)")
    BANNER_PAGINATION_BULLETS = (By.CSS_SELECTOR,
                                 ".swiper-pagination.slideshow0.swiper-pagination-clickable.swiper-pagination-bullets")
    HEADER_FEATURED = (By.TAG_NAME, "h3")
    CAROUSEL_BRAND = (By.CSS_SELECTOR, "#carousel0.swiper-container-horizontal")
    CAROUSEL_PAGINATION_BULLETS = (By.CSS_SELECTOR,
                                   ".swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets")


class ProductPageLocators:
    PRODUCT_HEADER = (By.CSS_SELECTOR, ".btn-group + h1")
    BUTTON_CART = (By.ID, "button-cart")
    IMAGES_BLOCK = (By.CLASS_NAME, "thumbnails")
    RATING_BLOCK = (By.CLASS_NAME, "rating")
    PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, "#tab-description > p")
    MAIN_PRODUCT_IMAGE = (By.XPATH, '//ul[@class="thumbnails"]/li[1]')
    PRODUCT_IMAGE_IN_WINDOW = (By.CSS_SELECTOR, ".mfp-figure")
    TAB_DESCRIPTION_CLASS = (By.XPATH, '//ul[@class="nav nav-tabs"]/li[1]')
    TAB_SPECIFICATION_CLASS = (By.XPATH, '//ul[@class="nav nav-tabs"]/li[2]')
    TAB_REVIEWS_CLASS = (By.XPATH, '//ul[@class="nav nav-tabs"]/li[3]')
    TAB_DESCRIPTION_LINK = (By.XPATH, '//a[@href="#tab-description"]')
    TAB_SPECIFICATION_LINK = (By.XPATH, '//a[@href="#tab-specification"]')
    TAB_REVIEWS_LINK = (By.XPATH, '//a[@href="#tab-review"]')


class CataloguePageLocators:
    BREADCRUMB = (By.CLASS_NAME, "breadcrumb")
    CATALOGUE_HEADER = (By.TAG_NAME, "h2")
    CATALOGUE_IMAGE = (By.CLASS_NAME, "img-thumbnail")
    LEFT_MENU = (By.ID, "column-left")
    BANNER_UNDER_LEFT_MENU = (By.ID, "banner0")
    FIRST_PRODUCT = (By.XPATH,
                     "/html/body/div[2]/div/div/div[4]/div[1]")
    COMPARE_BUTTON = (By.XPATH,
                      '//button[@data-original-title="Compare this Product" and contains(@onclick, "47")]')
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    COMPARE_LINK = (By.ID, "compare-total")
    SELECT_SORT = (By.ID, "input-sort")
    FIRST_PRODUCT_AFTER_SORT = (By.XPATH,
                                "/html/body/div[2]/div/div/div[4]/div[1]/div/div[2]/div[1]/h4/a")
    LAST_PRODUCT_AFTER_SORT = (By.XPATH,
                               "/html/body/div[2]/div/div/div[4]/div[5]/div/div[2]/div[1]/h4/a")


class LoginPageLocators:
    NEW_CUSTOMER_FORM = (By.CSS_SELECTOR,
                         "#content > .row > .col-sm-6:first-child >.well")
    OLD_CUSTOMER_FORM = (By.CSS_SELECTOR,
                         "#content > .row > .col-sm-6:last-child >.well")
    RIGHT_LIST_MENU = (By.CLASS_NAME, "list-group")
    BUTTON_FOR_NEW_CUSTOMER = (By.CSS_SELECTOR, "a.btn.btn-primary")
    BUTTON_FOR_OLD_CUSTOMER = (By.CSS_SELECTOR, "input.btn.btn-primary")


class AdminPageLocators:
    PANEL_HEADING = (By.CLASS_NAME, "panel-heading")
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-primary")
    HELP_BLOCK = (By.CLASS_NAME, "help-block")
    NEED_LOGIN_TEXT = (By.XPATH, "//h1[contains(text(), 'enter your login')]")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".nav > li:nth-child(2) > a")
    LEFT_MENU_CATALOGUE = (By.CSS_SELECTOR, "#menu-catalog > a")
    LEFT_MENU_CATEGORIES = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(1) > a")
    CATEGORIES_TABLE = (By.CSS_SELECTOR, ".table-responsive")
