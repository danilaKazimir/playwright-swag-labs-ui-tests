from pages.base_page import BasePage
from pages.constants import LoginPageConstants


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

    # Page methods
    def check_that_login_page_is_opened(self):
        self.check_page_url(LoginPageConstants.LOGIN_PAGE_URL)
        self.check_page_title(LoginPageConstants.LOGIN_PAGE_TITLE)
        self.check_swag_labs_logo()

    def close_error_message(self):
        self.error_message_x_button.click()
        self.check_element_is_hidden(self.username_field_error_img)
        self.check_element_is_hidden(self.password_field_error_img)
        self.check_element_is_hidden(self.error_message)
        self.check_element_is_hidden(self.error_message_x_button)

    def login_into_swag_labs(self, username, password, is_success_login=True, error_text=None):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.submit_button.click()
        if not is_success_login:
            self.check_element_is_visible(self.username_field_error_img)
            self.check_element_is_visible(self.password_field_error_img)
            self.check_element_text(self.error_message, error_text)
            self.check_element_is_visible(self.error_message_x_button)
            self.close_error_message()
