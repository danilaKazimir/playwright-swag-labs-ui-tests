from typing import Callable
from playwright.sync_api import Page, expect
from pages.constants import BasePageConstants


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.swag_labs_logo = self.get_element_by_text("Swag Labs", exact=True)
        self.page_header = self.get_element_by_test_id("title")
        self.footer_twitter_link = self.get_element_by_test_id("social-twitter")
        self.footer_facebook_link = self.get_element_by_test_id("social-facebook")
        self.footer_linkedin_link = self.get_element_by_test_id("social-linkedin")
        self.footer_copyright_text = self.get_element_by_test_id("footer-copy")
        self.open_burger_menu_button = self.get_element_by_locator("#react-burger-menu-btn")
        self.burger_menu_inner = self.get_element_by_locator(".bm-menu")
        self.burger_menu_all_item_link = self.get_element_by_role("link", "All Items")
        self.burger_menu_about_link = self.get_element_by_role("link", "About")
        self.burger_menu_logout_link = self.get_element_by_role("link", "Logout")
        self.burger_menu_close_button = self.get_element_by_locator("#react-burger-cross-btn")
        self.cart = self.get_element_by_test_id("shopping-cart-link")
        self.cart_badge = self.get_element_by_test_id("shopping-cart-badge")

    def open_page(self, url):
        self.page.goto(url)

    def get_element_by_role(self, role, name):
        return self.page.get_by_role(role, name=name)

    def get_element_by_placeholder(self, placeholder):
        return self.page.get_by_placeholder(placeholder)

    def get_element_by_test_id(self, test_id):
        return self.page.get_by_test_id(test_id)

    def get_element_by_locator(self, locator):
        return self.page.locator(locator)

    def get_element_by_text(self, locator, exact=False):
        return self.page.get_by_text(locator, exact=exact)

    def check_element_is_visible(self, element):
        expect(element).to_be_visible()

    def check_element_is_hidden(self, element):
        expect(element).to_be_hidden()

    def check_element_text(self, element, expected_text):
        expect(element).to_have_text(expected_text)

    def check_element_attribute(self, element, attr, exp_attr_value):
        expect(element).to_have_attribute(attr, exp_attr_value)

    def check_page_url(self, url):
        expect(self.page).to_have_url(url)

    def check_page_title(self, title):
        expect(self.page).to_have_title(title)

    def check_page_header(self, page_header):
        self.check_element_text(self.page_header, page_header)

    def check_swag_labs_logo(self):
        self.check_element_text(self.swag_labs_logo, BasePageConstants.SWAG_LABS_LOGO)

    def open_new_browser_tab_page_by_action(self, action: Callable[[], None]) -> None:
        """Open a new browser tab after some action and change the context to the opened tab"""
        with self.page.context.expect_page() as new_page:
            action()
        self.page = new_page.value

    def send_get_request(self, endpoint):
        return self.page.request.get(endpoint).json()

    # Methods with footer elements
    def open_twitter_link(self):
        self.open_new_browser_tab_page_by_action(self.footer_twitter_link.click)
        self.check_page_url(BasePageConstants.TWITTER_PAGE_URL)
        self.check_page_title(BasePageConstants.TWITTER_PAGE_TITLE)

    def open_facebook_link(self):
        self.open_new_browser_tab_page_by_action(self.footer_facebook_link.click)
        self.check_page_url(BasePageConstants.FACEBOOK_PAGE_URL)
        self.check_page_title(BasePageConstants.FACEBOOK_PAGE_TITLE)

    def open_linkedin_link(self):
        self.open_new_browser_tab_page_by_action(self.footer_linkedin_link.click)
        self.check_page_url(BasePageConstants.LINKEDIN_PAGE_URL)
        self.check_page_title(BasePageConstants.LINKEDIN_PAGE_TITLE)

    def check_footer_copyright_text(self):
        self.check_element_text(self.footer_copyright_text, BasePageConstants.FOOTER_COPYRIGHT_TEXT)

    # Methods with burger menu
    def open_burger_menu(self):
        self.open_burger_menu_button.click()
        self.check_element_is_visible(self.burger_menu_inner)

    def open_about_link(self):
        self.burger_menu_about_link.click()
        self.check_page_url(BasePageConstants.SAUCE_LABS_COM_URL)
        self.check_page_title(BasePageConstants.SAUCE_LABS_COM_TITLE)

    def click_on_all_item_link(self):
        self.burger_menu_all_item_link.click()

    def close_burger_menu(self):
        self.burger_menu_close_button.click()
        self.check_element_is_hidden(self.burger_menu_inner)

    def logout(self):
        self.burger_menu_logout_link.click()

    # Methods with shopping cart
    def check_that_cart_badge_value_is_correct(self, expected_value):
        self.check_element_text(self.cart_badge, expected_value)

    def check_that_cart_badge_is_not_displayed(self):
        self.check_element_is_hidden(self.cart_badge)

    def click_on_cart(self):
        self.cart.click()
