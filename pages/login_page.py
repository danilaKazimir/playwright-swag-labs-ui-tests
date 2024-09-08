from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = 'https://www.saucedemo.com/'

    # Page elements
    def get_username_field(self):
        return self.get_element_by_placeholder("Username")

    def get_password_field(self):
        return self.get_element_by_placeholder("Password")

    def get_submit_button(self):
        return self.get_element_by_role("button", "Login")

    # Methods
    def login_into_swag_labs(self):
        self.get_username_field().fill("standard_user")
        self.get_password_field().fill("secret_sauce")
        self.get_submit_button().click()
