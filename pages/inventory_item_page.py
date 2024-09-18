from pages.base_page import BasePage
from pages.constants import InventoryItemPageConstants


class InventoryItemPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.expected_item_values = None
        self.back_to_products_link = self.get_element_by_test_id("back-to-products")
        self.item_name = self.get_element_by_test_id("inventory-item-name")
        self.item_description = self.get_element_by_test_id("inventory-item-desc")
        self.item_price = self.get_element_by_test_id("inventory-item-price")
        self.item_image = self.get_element_by_locator(".inventory_details_img")
        self.item_button = self.get_element_by_locator(".btn_inventory")

    # Additional helping method
    def get_single_item_values_from_mock_api(self, endpoint, item):
        return self.send_get_request(endpoint)[item]

    # Page method
    def check_that_inventory_item_page_is_opened(self):
        self.check_page_url(f"{InventoryItemPageConstants.INVENTORY_ITEM_BASE_URL}{self.expected_item_values["id"]}")
        self.check_page_title(InventoryItemPageConstants.INVENTORY_ITEM_TITLE)
        self.check_swag_labs_logo()

    def click_on_back_to_products_link(self):
        self.back_to_products_link.click()

    def click_on_item_button(self):
        self.item_button.click()

    def check_that_item_button_text_is_correct(self, expected_value):
        self.check_element_text(self.item_button, expected_value)

    def check_item_values(self):
        self.check_element_text(self.item_name, self.expected_item_values["name"])
        self.check_element_text(self.item_description, self.expected_item_values["description"])
        self.check_element_text(self.item_price, self.expected_item_values["price"])
        self.check_element_is_visible(self.item_button)
        self.check_element_attribute(self.item_image, "src", self.expected_item_values['image'])
