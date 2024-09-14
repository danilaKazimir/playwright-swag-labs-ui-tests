from pages.base_page import BasePage
from pages.locators import InventoryPageLocators
from pages.constants import InventoryPageConstants, LoginPageConstants


class InventoryPage(BasePage):
    # Get page elements
    def get_twitter_link(self):
        return self.get_element_by_test_id(InventoryPageLocators.TWITTER_LINK_DATA_TEST_VALUE)

    def get_facebook_link(self):
        return self.get_element_by_test_id(InventoryPageLocators.FACEBOOK_LINK_DATA_TEST_VALUE)

    def get_linkedin_link(self):
        return self.get_element_by_test_id(InventoryPageLocators.LINKEDIN_LINK_DATA_TEST_VALUE)

    def get_footer_copyright_text(self):
        return self.get_element_by_test_id(InventoryPageLocators.FOOTER_COPYRIGHT_TEXT_DATA_TEST_VALUE)

    def get_burger_button(self):
        return self.get_element_by_locator(InventoryPageLocators.BURGER_BUTTON)

    def get_about_link(self):
        return self.get_element_by_role("link", InventoryPageLocators.SAUCE_LABS_COM_LINK_VALUE)

    def get_logout_link(self):
        return self.get_element_by_role("link", InventoryPageLocators.LOGOUT_LINK_VALUE)

    # Actions
    def click_on_twitter_link(self):
        self.get_twitter_link().click()

    def click_on_facebook_link(self):
        self.get_facebook_link().click()

    def click_on_linkedin_link(self):
        self.get_linkedin_link().click()

    def click_on_burger_button(self):
        self.get_burger_button().click()

    def click_on_about_link(self):
        self.get_about_link().click()

    def click_on_logout_link(self):
        self.get_logout_link().click()

    # Methods
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
        self.check_element_text(self.get_footer_copyright_text(), InventoryPageConstants.FOOTER_COPYRIGHT_TEXT)

    def open_about_link(self):
        self.click_on_burger_button()
        self.click_on_about_link()
        self.check_page_url(InventoryPageConstants.SAUCE_LABS_COM_URL)
        self.check_page_title(InventoryPageConstants.SAUCE_LABS_COM_TITLE)

    def logout(self):
        self.click_on_burger_button()
        self.click_on_logout_link()
        self.check_page_url(LoginPageConstants.LOGIN_PAGE_URL)
        self.check_page_title(LoginPageConstants.LOGIN_PAGE_TITLE)
