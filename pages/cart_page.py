from pages.base_page import BasePage
from pages.constants import CartPageConstants


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.expected_item_values = None
        self.item_name = self.get_element_by_test_id("inventory-item-name")
        self.item_description = self.get_element_by_test_id("inventory-item-desc")
        self.item_price = self.get_element_by_test_id("inventory-item-price")
        self.item_button = self.get_element_by_locator(".cart_button")
        self.item_quantity = self.get_element_by_test_id("item-quantity")
        self.continue_shopping_btn = self.get_element_by_role("button", "Continue Shopping")
        self.checkout_btn = self.get_element_by_role("button", "Checkout")
        self.cart_item_div = self.get_element_by_locator(".cart_item")

    # Additional helping method
    def get_single_item_values_from_mock_api(self, endpoint, item):
        return self.send_get_request(endpoint)[item]

    # Page method
    def check_that_cart_page_is_opened(self):
        self.check_page_url(CartPageConstants.CART_PAGE_URL)
        self.check_page_title(CartPageConstants.CART_PAGE_TITLE)
        self.check_page_header(CartPageConstants.CART_PAGE_HEADER)
        self.check_swag_labs_logo()

    def click_on_continue_shopping_btn(self):
        self.continue_shopping_btn.click()

    def click_on_checkout_button(self):
        self.checkout_btn.click()

    def click_on_item_remove_button(self):
        self.item_button.click()

    def check_item_values(self):
        self.check_element_text(self.item_name, self.expected_item_values["name"])
        self.check_element_text(self.item_description, self.expected_item_values["description"])
        self.check_element_text(self.item_price, self.expected_item_values["price"])
        self.check_element_is_visible(self.item_button)
        self.check_element_text(self.item_quantity, "1")

    def check_that_item_is_not_displayed(self):
        self.check_element_is_hidden(self.cart_item_div)

    def check_that_item_is_displayed(self):
        self.check_element_is_visible(self.cart_item_div)
