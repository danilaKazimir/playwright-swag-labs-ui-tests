from pages.base_page import BasePage
from pages.constants import InventoryPageConstants


class LoginPage(BasePage):
    # Get page elements
    def get_username_field(self):
        return self.get_element_by_placeholder("Username")

    def get_password_field(self):
        return self.get_element_by_placeholder("Password")

    def get_submit_button(self):
        return self.get_element_by_role("button", "Login")

    def get_username_field_error_img(self):
        return self.get_element_by_locator("svg").first

    def get_password_field_error_img(self):
        return self.get_element_by_locator("svg").nth(1)

    def get_error_message(self):
        return self.get_element_by_test_id("error")

    def get_error_message_x_button(self):
        return self.get_element_by_test_id("error-button")

    # Actions
    def fill_username_field(self, username):
        self.get_username_field().fill(username)

    def fill_password_field(self, password):
        self.get_password_field().fill(password)

    def click_on_submit_button(self):
        self.get_submit_button().click()

    def close_error_message(self):
        self.get_error_message_x_button().click()
        self.check_element_is_hidden(self.get_username_field_error_img())
        self.check_element_is_hidden(self.get_password_field_error_img())
        self.check_element_is_hidden(self.get_error_message())
        self.check_element_is_hidden(self.get_error_message_x_button())

    # Methods
    def login_into_swag_labs(self, username, password, is_success_login=True, error_text=None):
        self.fill_username_field(username)
        self.fill_password_field(password)
        self.click_on_submit_button()
        if is_success_login:
            self.check_page_url(InventoryPageConstants.INVENTORY_PAGE_URL)
            self.check_page_title(InventoryPageConstants.INVENTORY_PAGE_TITLE)
        else:
            self.check_element_is_visible(self.get_username_field_error_img())
            self.check_element_is_visible(self.get_password_field_error_img())
            self.check_element_is_visible(self.get_error_message())
            self.check_element_text(self.get_error_message(), error_text)
            self.check_element_is_visible(self.get_error_message_x_button())
            self.close_error_message()
