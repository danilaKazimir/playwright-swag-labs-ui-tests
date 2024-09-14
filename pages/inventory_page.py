from pages.base_page import BasePage
from pages.locators import InventoryPageLocators
from pages.constants import InventoryPageConstants


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

    # Actions
    def click_on_twitter_link(self):
        self.get_twitter_link().click()

    def click_on_facebook_link(self):
        self.get_facebook_link().click()

    def click_on_linkedin_link(self):
        self.get_linkedin_link().click()

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
