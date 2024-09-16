from pages.base_page import BasePage
from pages.constants import InventoryItemPageConstants


class InventoryItemPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.expected_item_values = None
        self.back_to_products_link = self.get_element_by_test_id("back-to-products")

    # Additional helping method
    def get_single_item_values_from_mock_api(self, endpoint, item):
        return self.send_get_request(endpoint)[item]

    # Page method
    def check_that_inventory_item_page_is_opened(self):
        self.check_page_url(f"{InventoryItemPageConstants.INVENTORY_ITEM_BASE_URL}{self.expected_item_values["id"]}")
        self.check_page_title(InventoryItemPageConstants.INVENTORY_ITEM_TITLE)

    def click_on_back_to_products_link(self):
        self.back_to_products_link.click()
