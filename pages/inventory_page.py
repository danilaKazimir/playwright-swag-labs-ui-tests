from pages.base_page import BasePage
from pages.constants import InventoryPageConstants, LoginPageConstants


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.item_locators = None
        self.twitter_link = self.get_element_by_test_id("social-twitter")
        self.facebook_link = self.get_element_by_test_id("social-facebook")
        self.linkedin_link = self.get_element_by_test_id("social-linkedin")
        self.footer_copyright_text = self.get_element_by_test_id("footer-copy")
        self.open_burger_menu_button = self.get_element_by_locator("#react-burger-menu-btn")
        self.burger_menu_inner = self.get_element_by_locator(".bm-menu")
        self.about_link = self.get_element_by_role("link", "About")
        self.logout_link = self.get_element_by_role("link", "Logout")

    @property
    def item_name(self):
        return self.get_element_by_locator(self.item_locators['name'])

    @property
    def item_desc(self):
        return self.get_element_by_locator(self.item_locators['description'])

    @property
    def item_price(self):
        return self.get_element_by_locator(self.item_locators['price'])

    @property
    def item_img_url(self):
        return self.get_element_by_locator(self.item_locators['image'])

    @property
    def item_btn(self):
        return self.get_element_by_locator(self.item_locators['button'])

    # Page actions
    def click_on_twitter_link(self):
        self.twitter_link.click()

    def click_on_facebook_link(self):
        self.facebook_link.click()

    def click_on_linkedin_link(self):
        self.linkedin_link.click()

    def click_on_open_burger_menu_button(self):
        self.open_burger_menu_button.click()

    def click_on_about_link(self):
        self.about_link.click()

    def click_on_logout_link(self):
        self.logout_link.click()

    # Page methods
    def open_twitter_link(self):
        self.open_new_browser_tab_page_by_action(self.click_on_twitter_link)
        self.check_page_url(InventoryPageConstants.TWITTER_PAGE_URL)
        self.check_page_title(InventoryPageConstants.TWITTER_PAGE_TITLE)

    def open_facebook_link(self):
        self.open_new_browser_tab_page_by_action(self.click_on_facebook_link)
        self.check_page_url(InventoryPageConstants.FACEBOOK_PAGE_URL)
        self.check_page_title(InventoryPageConstants.FACEBOOK_PAGE_TITLE)

    def open_linkedin_link(self):
        self.open_new_browser_tab_page_by_action(self.click_on_linkedin_link)
        self.check_page_url(InventoryPageConstants.LINKEDIN_PAGE_URL)
        self.check_page_title(InventoryPageConstants.LINKEDIN_PAGE_TITLE)

    def check_footer_copyright_text(self):
        self.check_element_text(self.footer_copyright_text, InventoryPageConstants.FOOTER_COPYRIGHT_TEXT)

    def open_burger_menu(self):
        self.click_on_open_burger_menu_button()
        self.check_element_is_visible(self.burger_menu_inner)

    def open_about_link(self):
        self.click_on_about_link()
        self.check_page_url(InventoryPageConstants.SAUCE_LABS_COM_URL)
        self.check_page_title(InventoryPageConstants.SAUCE_LABS_COM_TITLE)

    def logout(self):
        self.click_on_logout_link()
        self.check_page_url(LoginPageConstants.LOGIN_PAGE_URL)
        self.check_page_title(LoginPageConstants.LOGIN_PAGE_TITLE)

    def check_item_values(self):
        self.check_element_text(self.item_name, "Sauce Labs Backpack")
        self.check_element_text(self.item_desc, "carry.allTheThings() with the sleek, streamlined Sly "
                                                "Pack that melds uncompromising style with unequaled "
                                                "laptop and tablet protection.")
        self.check_element_text(self.item_price, "$29.99")
        self.check_element_is_visible(self.item_btn)
        self.check_element_attribute(self.item_img_url, "src", "/static/media/sauce-backpack-1200x1500.0a0b85a3.jpg")
