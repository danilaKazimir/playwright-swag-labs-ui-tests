from pages.base_page import BasePage
from pages.constants import InventoryItemPageConstants


class InventoryItemPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.expected_item_values = None

    # Additional helping method
    def get_single_item_values_from_mock_api(self, endpoint, item):
        return self.send_get_request(endpoint)[item]

    def check_that_inventory_item_page_is_opened(self):
        self.check_page_url(f"{InventoryItemPageConstants.INVENTORY_ITEM_BASE_URL}{self.expected_item_values["id"]}")
        self.check_page_title(InventoryItemPageConstants.INVENTORY_ITEM_TITLE)
