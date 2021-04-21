from selenium.webdriver.common.by import By


def test_assert_main_page(browser, url):
    """Test main page title"""
    browser.get(url)
    assert browser.title == "Your Store", "Wrong title"


def test_main_page_elements_is_displayed(browser, url, fixture_find_element):
    """Test elements on main page"""
    browser.get(url)
    # banner
    fixture_find_element.find_visible_element(browser, By.CSS_SELECTOR,
                                              "#content .swiper-viewport:nth-child(1)",
                                              "Banner is not displayed")
    # banner pagination bullets
    fixture_find_element.find_visible_element(browser, By.CSS_SELECTOR,
                                              ".swiper-pagination.slideshow0.swiper-pagination-clickable.swiper-pagination-bullets",
                                              "Slideshow pagination bullets are not displayed")
    # header Featured
    fixture_find_element.find_visible_element(browser, By.TAG_NAME,
                                              "h3", "Header is not displayed")
    # carousel brand
    fixture_find_element.find_visible_element(browser, By.CSS_SELECTOR,
                                              "#carousel0.swiper-container-horizontal",
                                              "Carousel brand is not displayed")
    # carousel pagination bullets
    fixture_find_element.find_visible_element(browser, By.CSS_SELECTOR,
                                              ".swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets",
                                              "Carousel pagination bullets are not displayed")


def test_catalogue_page_elements_is_displayed(browser, url, fixture_find_element):
    """Test elements on catalogue page"""
    browser.get(f'{url}index.php?route=product/category&path=18')

    # bread_crumb
    fixture_find_element.find_visible_element(browser, By.CLASS_NAME,
                                              "breadcrumb",
                                              "Breadcrump is not displayed")
    # header
    fixture_find_element.find_visible_element(browser, By.TAG_NAME,
                                              "h2",
                                              "Header of catalogue is not displayed")
    # catalogue img
    fixture_find_element.find_visible_element(browser, By.CLASS_NAME,
                                              "img-thumbnail",
                                              "Image of catalogue is not displayed")
    # left menu
    fixture_find_element.find_visible_element(browser, By.ID,
                                              "column-left",
                                              "Left menu is not displayed")
    # banner under left menu
    fixture_find_element.find_visible_element(browser, By.ID,
                                              "banner0",
                                              "Banner is not displayed")


def test_product_page_elements_is_displayed(browser, url, fixture_find_element):
    """Test elements on product page"""
    browser.get(f'{url}index.php?route=product/product&path=18&product_id=47')
    # product header
    fixture_find_element.find_visible_element(browser, By.CSS_SELECTOR,
                                              ".btn-group + h1",
                                              "Header is not displayed")
    # button cart
    fixture_find_element.find_visible_element(browser, By.ID,
                                              "button-cart",
                                              "Button cart is not displayed")
    # images block
    fixture_find_element.find_visible_element(browser, By.CLASS_NAME,
                                              "thumbnails",
                                              "Block of images is not displayed")
    # rating block
    fixture_find_element.find_visible_element(browser, By.CLASS_NAME,
                                              "rating",
                                              "Rating block is not displayed")
    # product description
    fixture_find_element.find_visible_element(browser, By.CSS_SELECTOR,
                                              "#tab-description > p",
                                              "Product description is not displayed")


def test_user_login_page_elements_is_displayed(browser, url, fixture_find_element):
    """Test elements on user login page"""
    browser.get(f'{url}index.php?route=account/login')
    # new customer form
    fixture_find_element.find_visible_element(browser, By.CSS_SELECTOR,
                                              "#content > .row > .col-sm-6:first-child >.well",
                                              "Form for new customer is not displayed")
    # old customer form
    fixture_find_element.find_visible_element(browser, By.CSS_SELECTOR,
                                              "#content > .row > .col-sm-6:last-child >.well",
                                              "Form for old customer is not displayed")

    # right list menu
    fixture_find_element.find_visible_element(browser, By.CLASS_NAME,
                                              "list-group",
                                              "Right menu list is not displayed")

    # button for new customer form
    fixture_find_element.find_visible_element(browser, By.CSS_SELECTOR,
                                              "a.btn.btn-primary",
                                              "Button in new customer form is not displayed")
    # button for old customer form
    fixture_find_element.find_visible_element(browser, By.CSS_SELECTOR,
                                              "input.btn.btn-primary",
                                              "Button in old customer form is not displayed")


def test_admin_login_page_elements_is_displayed(browser, url, fixture_find_element):
    """Test elements on admin login page"""
    browser.get(f'{url}admin/')
    # panel heading
    fixture_find_element.find_visible_element(browser, By.CLASS_NAME,
                                              "panel-heading",
                                              "Panel heading is not displayed")
    # username input
    fixture_find_element.find_visible_element(browser, By.ID,
                                              "input-username",
                                              "Username input is not displayed")
    # password input
    fixture_find_element.find_visible_element(browser, By.ID,
                                              "input-password",
                                              "Password input is not displayed")
    # login button
    fixture_find_element.find_visible_element(browser, By.CSS_SELECTOR,
                                              "button.btn.btn-primary",
                                              "Login button is not displayed")
    # help block
    fixture_find_element.find_visible_element(browser, By.CLASS_NAME,
                                              "help-block",
                                              "Help block is not displayed")


def test_login_action(browser, url, fixture_find_element):
    """Test login to admin panel"""
    browser.get(f'{url}admin/')
    username_input = fixture_find_element.find_visible_element(browser, By.ID,
                                              "input-username",
                                              "Username input is not displayed")
    password_input = fixture_find_element.find_visible_element(browser, By.ID,
                                              "input-password",
                                              "Password input is not displayed")
    login_button = fixture_find_element.find_visible_element(browser, By.CSS_SELECTOR,
                                              "button.btn.btn-primary",
                                              "Login button is not displayed")

    username_input.clear()
    username_input.send_keys("demo")
    password_input.clear()
    password_input.send_keys("demo")
    login_button.click()
    fixture_find_element.assert_title(browser, "Dashboard",
                                      "Title is wrong")


def test_logout_action(browser, url, fixture_find_element):
    """Test logout from admin panel"""
    browser.get(f'{url}admin/')
    username_input = fixture_find_element.find_visible_element(browser, By.ID,
                                              "input-username",
                                              "Username input is not displayed")
    password_input = fixture_find_element.find_visible_element(browser, By.ID,
                                              "input-password",
                                              "Password input is not displayed")
    login_button = fixture_find_element.find_visible_element(browser, By.CSS_SELECTOR,
                                              "button.btn.btn-primary",
                                              "Login button is not displayed")
    username_input.clear()
    username_input.send_keys("demo")
    password_input.clear()
    password_input.send_keys("demo")
    login_button.click()
    logout_button = fixture_find_element.wait_clickable_el(browser, By.CSS_SELECTOR,
                                                           ".nav > li:nth-child(2) > a",
                                                           "Logout button is not displayed and not clickable")
    logout_button.click()
    fixture_find_element.find_visible_element(browser, By.XPATH,
                                              "//h1[contains(text(), 'enter your login')]",
                                              "Fail logout")


def test_go_to_products_table(browser, url, fixture_find_element):
    """Test go to products table in admin panel"""
    browser.get(f'{url}admin/')
    username_input = fixture_find_element.find_visible_element(browser, By.ID,
                                              "input-username",
                                              "Username input is not displayed")
    password_input = fixture_find_element.find_visible_element(browser, By.ID,
                                              "input-password",
                                              "Password input is not displayed")
    login_button = fixture_find_element.find_visible_element(browser, By.CSS_SELECTOR,
                                              "button.btn.btn-primary",
                                              "Login button is not displayed")

    username_input.clear()
    username_input.send_keys("demo")
    password_input.clear()
    password_input.send_keys("demo")
    login_button.click()
    catalog = fixture_find_element.find_visible_element(browser, By.CSS_SELECTOR,
                                                        "#menu-catalog > a",
                                                        "Catalogue is not displayed in menu")
    catalog.click()
    categories = fixture_find_element.find_visible_element(browser, By.CSS_SELECTOR,
                                                           "#collapse1 > li:nth-child(1) > a",
                                                           "Categories is not displayed in menu")
    categories.click()
    fixture_find_element.find_visible_element(browser, By.CSS_SELECTOR,
                                              ".table-responsive",
                                              "Table with products is not displayed")
