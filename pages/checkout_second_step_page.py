from pages.base_page import BasePage
from pages.constants import CheckoutSecondStepConstants


class CheckoutSecondStepPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.item_total_label = self.get_element_by_test_id("subtotal-label")
        self.item_tax_label = self.get_element_by_test_id("tax-label")
        self.price_total_value = self.get_element_by_test_id("total-label")
        self.cancel_button = self.get_element_by_role("button", "Cancel")
        self.finish_button = self.get_element_by_role("button", "Finish")

    # Page method
    def check_that_checkout_second_step_is_opened(self):
        self.check_page_url(CheckoutSecondStepConstants.CHECKOUT_SECOND_STEP_URL)
        self.check_page_title(CheckoutSecondStepConstants.CHECKOUT_SECOND_STEP_TITLE)
        self.check_page_header(CheckoutSecondStepConstants.CHECKOUT_SECOND_STEP_HEADER)
        self.check_swag_labs_logo()

    def click_on_cancel_button(self):
        self.cancel_button.click()

    def click_on_finish_button(self):
        self.finish_button.click()
