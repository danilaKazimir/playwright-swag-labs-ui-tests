from pages.base_page import BasePage
from pages.constants import CheckoutFinishConstants


class CheckoutFinishPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.pony_express_image = self.get_element_by_test_id("pony-express")
        self.complete_header = self.get_element_by_test_id("complete-header")
        self.complete_text = self.get_element_by_test_id("complete-text")
        self.back_home_button = self.get_element_by_role("button", "Back Home")

    # Page methods
    def check_that_checkout_finish_page_is_opened(self):
        self.check_page_url(CheckoutFinishConstants.CHECKOUT_FINISH_URL)
        self.check_page_title(CheckoutFinishConstants.CHECKOUT_FINISH_TITLE)
        self.check_page_header(CheckoutFinishConstants.CHECKOUT_FINISH_HEADER)
        self.check_swag_labs_logo()

    def check_that_pony_express_image_is_displayed(self):
        self.check_element_is_visible(self.pony_express_image)

    def check_that_complete_header_text_is_correct(self):
        self.check_element_text(self.complete_header, CheckoutFinishConstants.COMPLETE_HEADER)

    def check_that_complete_text_is_correct(self):
        self.check_element_text(self.complete_text, CheckoutFinishConstants.COMPLETE_TEXT)

    def click_on_back_home_button(self):
        self.back_home_button.click()
