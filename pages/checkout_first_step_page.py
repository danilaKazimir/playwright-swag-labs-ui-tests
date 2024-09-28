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

    def click_on_cancel_button(self):
        self.cancel_button.click()

    def click_on_continue_button(self):
        self.continue_button.click()
