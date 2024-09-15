from pages.base_page import BasePage
from pages.constants import InventoryPageConstants


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_field = self.get_element_by_placeholder("Username")
        self.password_field = self.get_element_by_placeholder("Password")
        self.submit_button = self.get_element_by_role("button", "Login")
        self.error_message = self.get_element_by_test_id("error")
        self.username_field_error_img = self.get_element_by_locator(".form_group svg").first
        self.password_field_error_img = self.get_element_by_locator(".form_group svg").last
        self.error_message_x_button = self.get_element_by_test_id("error-button")

    # Page actions
    def fill_username_field(self, username):
        self.username_field.fill(username)

    def fill_password_field(self, password):
        self.password_field.fill(password)

    def click_on_submit_button(self):
        self.submit_button.click()

    def close_error_message(self):
        self.error_message_x_button.click()
        self.check_element_is_hidden(self.username_field_error_img)
        self.check_element_is_hidden(self.password_field_error_img)
        self.check_element_is_hidden(self.error_message)
        self.check_element_is_hidden(self.error_message_x_button)

    # Page methods
    def login_into_swag_labs(self, username, password, is_success_login=True, error_text=None):
        self.fill_username_field(username)
        self.fill_password_field(password)
        self.click_on_submit_button()
        if is_success_login:
            self.check_page_url(InventoryPageConstants.INVENTORY_PAGE_URL)
            self.check_page_title(InventoryPageConstants.INVENTORY_PAGE_TITLE)
        else:
            self.check_element_is_visible(self.username_field_error_img)
            self.check_element_is_visible(self.password_field_error_img)
            self.check_element_text(self.error_message, error_text)
            self.check_element_is_visible(self.error_message_x_button)
            self.close_error_message()
