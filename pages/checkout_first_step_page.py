from pages.base_page import BasePage
from pages.constants import CheckoutFirstStepConstants


class CheckoutFirstStepPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name_input = self.get_element_by_placeholder("First Name")
        self.last_name_input = self.get_element_by_placeholder("Last Name")
        self.zip_code_input = self.get_element_by_placeholder("Zip/Postal Code")
        self.cancel_button = self.get_element_by_role("button", "Cancel")
        self.continue_button = self.get_element_by_role("button", "Continue")
        self.error_message = self.get_element_by_test_id("error")
        self.error_message_close_button = self.get_element_by_test_id("error-button")
        self.first_name_error_icon = self.get_element_by_locator(".error_icon").nth(0)
        self.last_name_error_icon = self.get_element_by_locator(".error_icon").nth(1)
        self.zip_code_error_icon = self.get_element_by_locator(".error_icon").nth(2)

    # Page method
    def check_that_checkout_first_step_page_is_opened(self):
        self.check_page_url(CheckoutFirstStepConstants.CHECKOUT_FIRST_STEP_URL)
        self.check_page_title(CheckoutFirstStepConstants.CHECKOUT_FIRST_STEP_TITLE)
        self.check_page_header(CheckoutFirstStepConstants.CHECKOUT_FIRST_STEP_HEADER)
        self.check_swag_labs_logo()

    def fill_first_name_input(self, value):
        self.first_name_input.fill(value)

    def fill_last_name_input(self, value):
        self.last_name_input.fill(value)

    def fill_zip_code_input(self, value):
        self.zip_code_input.fill(value)

    def fill_all_field(self, first_name, last_name, zip_code):
        self.fill_first_name_input(first_name)
        self.fill_last_name_input(last_name)
        self.fill_zip_code_input(zip_code)

    def click_on_cancel_button(self):
        self.cancel_button.click()

    def click_on_continue_button(self):
        self.continue_button.click()

    def check_that_field_error_icons_are_displayed(self):
        self.check_element_is_visible(self.first_name_error_icon)
        self.check_element_is_visible(self.last_name_error_icon)
        self.check_element_is_visible(self.zip_code_error_icon)

    def check_that_field_error_icons_are_not_visible(self):
        self.check_element_is_hidden(self.first_name_error_icon)
        self.check_element_is_hidden(self.last_name_error_icon)
        self.check_element_is_hidden(self.zip_code_error_icon)

    def check_that_error_message_displayed_correctly(self, expected_value):
        self.check_element_text(self.error_message, expected_value)

    def check_that_error_message_is_not_visible(self):
        self.check_element_is_hidden(self.error_message)

    def click_on_error_message_close_button(self):
        self.error_message_close_button.click()
