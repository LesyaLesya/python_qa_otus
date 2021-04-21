import time


class TestMainPage:
    def test_assert_title_main_page(self, browser, url):
        browser.get(url)
        assert browser.title == "Your Store", "Wrong title"

    def test_main_banner(self, browser, url):
        browser.get(url)
        banner = browser.find_element_by_css_selector("#content .swiper-viewport:nth-child(1)")
        assert banner.is_displayed(), "Banner is not displayed"

    def test_banner_pagination_bullets(self, browser, url):
        browser.get(url)
        pagination_bullets = browser.find_element_by_css_selector(
            ".swiper-pagination.slideshow0.swiper-pagination-clickable.swiper-pagination-bullets")
        assert pagination_bullets.is_displayed(), "Slideshow pagination bullets are not displayed"

    def test_header_featured(self, browser, url):
        browser.get(url)
        header = browser.find_element_by_tag_name("h3")
        assert header.text == "Featured", "Wrong header"

    def test_brand_carousel(self, browser, url):
        browser.get(url)
        carousel_brand = browser.find_element_by_css_selector("#carousel0.swiper-container-horizontal")
        assert carousel_brand.is_displayed(), "Carousel brand is not displayed"

    def test_carousel_pagination_bullets(self, browser, url):
        browser.get(url)
        pagination_bullets = browser.find_element_by_css_selector(
            ".swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets")
        assert pagination_bullets.is_displayed(), "Carousel pagination bullets are not displayed"


class TestCataloguePage:
    def test_bread_crump(self, browser, url):
        browser.get(f'{url}index.php?route=product/category&path=18')
        bread_crump = browser.find_element_by_class_name("breadcrumb")
        assert bread_crump.is_displayed(), "Breadcrump is not displayed"

    def test_catalogue_header(self, browser, url):
        browser.get(f'{url}index.php?route=product/category&path=18')
        header = browser.find_element_by_tag_name("h2")
        assert header.text == "Laptops & Notebooks", "Wrong header"

    def test_catalogue_img(self, browser, url):
        browser.get(f'{url}index.php?route=product/category&path=18')
        catalogue_img = browser.find_element_by_class_name("img-thumbnail")
        assert catalogue_img.is_displayed(), "Image of catalogue is not displayed"

    def test_left_menu(self, browser, url):
        browser.get(f'{url}index.php?route=product/category&path=18')
        left_menu = browser.find_element_by_id("column-left")
        assert left_menu.is_displayed(), "Left menu is not displayed"

    def test_banner_under_left_menu(self, browser, url):
        browser.get(f'{url}index.php?route=product/category&path=18')
        banner_under_left_menu = browser.find_element_by_id("banner0")
        assert banner_under_left_menu.is_displayed(), "Banner is not displayed"


class TestProductPage:
    def test_product_header(self, browser, url):
        browser.get(f'{url}index.php?route=product/product&path=18&product_id=47')
        product_header = browser.find_element_by_css_selector(".btn-group + h1")
        assert product_header.text == "HP LP3065", "Wrong header text"

    def test_button_cart(self, browser, url):
        browser.get(f'{url}index.php?route=product/product&path=18&product_id=47')
        button_cart = browser.find_element_by_id("button-cart")
        assert button_cart.is_displayed(), "Button cart is not displayed"

    def test_images_block(self, browser, url):
        browser.get(f'{url}index.php?route=product/product&path=18&product_id=47')
        images_block = browser.find_element_by_class_name("thumbnails")
        assert images_block.is_displayed(), "Block of images is not displayed"

    def test_rating_block(self, browser, url):
        browser.get(f'{url}index.php?route=product/product&path=18&product_id=47')
        rating_block = browser.find_element_by_class_name("rating")
        assert rating_block.is_displayed(), "Rating block is not displayed"

    def test_product_description(self, browser, url):
        browser.get(f'{url}index.php?route=product/product&path=18&product_id=47')
        product_description = browser.find_element_by_css_selector("#tab-description > p")
        assert product_description.is_displayed(), "Product description is not displayed"


class TestUserLogin:
    def test_new_customer_block(self, browser, url):
        browser.get(f'{url}index.php?route=account/login')
        new_customer = browser.find_element_by_css_selector("#content > .row > .col-sm-6:first-child >.well")
        assert new_customer.is_displayed(), "Form for new customer is not displayed"

    def test_old_customer_block(self, browser, url):
        browser.get(f'{url}index.php?route=account/login')
        old_customer = browser.find_element_by_css_selector("#content > .row > .col-sm-6:last-child >.well")
        assert old_customer.is_displayed(), "Form for old customer is not displayed"

    def test_right_list_menu(self, browser, url):
        browser.get(f'{url}index.php?route=account/login')
        right_list_menu = browser.find_element_by_class_name("list-group")
        assert right_list_menu.is_displayed(), "Right menu list is not displayed"

    def test_button_for_new_customer(self, browser, url):
        browser.get(f'{url}index.php?route=account/login')
        button_for_new_customer = browser.find_element_by_css_selector("a.btn.btn-primary")
        assert button_for_new_customer.is_displayed(), "Button is not displayed"
        assert button_for_new_customer.text == "Continue", "Text is not 'continue'"

    def test_button_for_old_customer(self, browser, url):
        browser.get(f'{url}index.php?route=account/login')
        button_for_old_customer = browser.find_element_by_css_selector("input.btn.btn-primary")
        assert button_for_old_customer.is_displayed(), "Button is not displayed"
        assert button_for_old_customer.get_attribute("value") == "Login", "Text is not 'login'"


class TestAdminLogin:
    def test_panel_heading(self, browser, url):
        browser.get(f'{url}admin/')
        panel_heading = browser.find_element_by_class_name("panel-heading")
        assert panel_heading.is_displayed(), "Panel heading is not displayed"

    def test_username_input(self, browser, url):
        browser.get(f'{url}admin/')
        username_input = browser.find_element_by_id("input-username")
        assert username_input.is_displayed(), "Username input is not displayed"

    def test_password_input(self, browser, url):
        browser.get(f'{url}admin/')
        password_input = browser.find_element_by_id("input-password")
        assert password_input.is_displayed(), "Password input is not displayed"

    def test_login_button(self, browser, url):
        browser.get(f'{url}admin/')
        login_button = browser.find_element_by_css_selector("button.btn.btn-primary")
        assert login_button.is_displayed(), "Login button is not displayed"

    def test_help_block(self, browser, url):
        browser.get(f'{url}admin/')
        help_block = browser.find_element_by_class_name("help-block")
        assert help_block.is_displayed(), "Help block is not displayed"


class TestAdminActions:
    def test_login(self, browser, url):
        browser.get(f'{url}admin/')
        username_input = browser.find_element_by_id("input-username")
        password_input = browser.find_element_by_id("input-password")
        login_button = browser.find_element_by_css_selector("button.btn.btn-primary")
        username_input.clear()
        username_input.send_keys("demo")
        password_input.clear()
        password_input.send_keys("demo")
        login_button.click()
        time.sleep(2)
        assert browser.title == "Dashboard", "Fail login"

    def test_logout(self, browser, url):
        browser.get(f'{url}admin/')
        username_input = browser.find_element_by_id("input-username")
        password_input = browser.find_element_by_id("input-password")
        login_button = browser.find_element_by_css_selector("button.btn.btn-primary")
        username_input.clear()
        username_input.send_keys("demo")
        password_input.clear()
        password_input.send_keys("demo")
        login_button.click()
        time.sleep(2)
        logout_button = browser.find_element_by_css_selector(".nav > li:nth-child(2) > a")
        logout_button.click()
        time.sleep(2)
        enter_login = browser.find_element_by_xpath(" //h1[contains(text(), 'enter your login')]")
        assert enter_login.is_displayed(), "Fail logout"

    def test_products_table(self, browser, url):
        browser.get(f'{url}admin/')
        username_input = browser.find_element_by_id("input-username")
        password_input = browser.find_element_by_id("input-password")
        login_button = browser.find_element_by_css_selector("button.btn.btn-primary")
        username_input.clear()
        username_input.send_keys("demo")
        password_input.clear()
        password_input.send_keys("demo")
        login_button.click()
        time.sleep(2)
        browser.find_element_by_css_selector("#menu-catalog > a").click()
        browser.find_element_by_css_selector("#collapse1 > li:nth-child(1) > a").click()
        assert browser.find_element_by_css_selector(".table-responsive").is_displayed(), "No table"
