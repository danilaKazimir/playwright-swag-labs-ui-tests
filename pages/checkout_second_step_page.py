from pages.base_page import BasePage
from pages.constants import CheckoutSecondStepConstants


class CheckoutSecondStepPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.expected_item_values = None
        self.item_name = self.get_element_by_test_id("inventory-item-name")
        self.item_description = self.get_element_by_test_id("inventory-item-desc")
        self.item_price = self.get_element_by_test_id("inventory-item-price")
        self.payment_information = self.get_element_by_test_id("payment-info-value")
        self.shipping_information = self.get_element_by_test_id("shipping-info-value")
        self.item_total_label = self.get_element_by_test_id("subtotal-label")
        self.item_tax_label = self.get_element_by_test_id("tax-label")
        self.price_total_value = self.get_element_by_test_id("total-label")
        self.cancel_button = self.get_element_by_role("button", "Cancel")
        self.finish_button = self.get_element_by_role("button", "Finish")

    # Additional helping method
    def get_single_item_values_from_mock_api(self, endpoint, item):
        return self.send_get_request(endpoint)[item]

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

    def check_item_values(self):
        self.check_element_text(self.item_name, self.expected_item_values["name"])
        self.check_element_text(self.item_description, self.expected_item_values["description"])
        self.check_element_text(self.item_price, self.expected_item_values["price"])

    def check_that_payment_information_is_correct(self):
        self.check_element_text(self.payment_information, CheckoutSecondStepConstants.SAUCE_CART)

    def check_that_shipping_information_is_correct(self):
        self.check_element_text(self.shipping_information, CheckoutSecondStepConstants.SHIPPING_OPTION)

    def check_that_item_total_label_is_correct(self):
        self.check_element_text(self.item_total_label, f'Item total: {self.expected_item_values["price"]}')

    def check_that_item_tax_label_is_correct(self):
        price = float(self.expected_item_values["price"][1:])
        expected_tax = "{:.2f}".format(round(price * 8 / 100, 2))
        self.check_element_text(self.item_tax_label, f'Tax: ${expected_tax}')

    def check_that_price_total_value_is_correct(self):
        price = float(self.expected_item_values["price"][1:])
        tax = round(price * 8 / 100, 2)
        expected_total_value = "{:.2f}".format(price + tax)
        self.check_element_text(self.price_total_value, f'Total: ${expected_total_value}')
