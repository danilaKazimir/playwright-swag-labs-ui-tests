from pages.base_page import BasePage
from pages.constants import InventoryPageConstants, ExceptionText


class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.item_locators = None
        self.expected_item_values = None

    @property
    def item_name(self):
        return self.get_element_by_locator(self.item_locators['name'])

    @property
    def item_desc(self):
        return self.get_element_by_locator(self.item_locators['description'])

    @property
    def item_price(self):
        return self.get_element_by_locator(self.item_locators['price'])

    @property
    def item_img(self):
        return self.get_element_by_locator(self.item_locators['image'])

    @property
    def item_btn(self):
        return self.get_element_by_locator(self.item_locators['button'])

    # Additional helping method
    def get_single_item_values_from_mock_api(self, endpoint, item):
        return self.send_get_request(endpoint)[item]

    # Page method
    def check_that_inventory_page_is_opened(self):
        self.check_page_url(InventoryPageConstants.INVENTORY_PAGE_URL)
        self.check_page_title(InventoryPageConstants.INVENTORY_PAGE_TITLE)
        self.check_page_header(InventoryPageConstants.INVENTORY_PAGE_HEADER)
        self.check_swag_labs_logo()

    def check_item_values(self):
        self.check_element_text(self.item_name, self.expected_item_values["name"])
        self.check_element_text(self.item_desc, self.expected_item_values["description"])
        self.check_element_text(self.item_price, self.expected_item_values["price"])
        self.check_element_is_visible(self.item_btn)
        self.check_element_attribute(self.item_img, "src", self.expected_item_values['image'])

    def click_on_item_name_link(self):
        try:
            self.item_name.click()
        except TypeError:
            raise Exception(ExceptionText.ITEM_NOT_SPECIFIED)

    def click_on_item_image_link(self):
        try:
            self.item_img.click()
        except TypeError:
            raise Exception(ExceptionText.ITEM_NOT_SPECIFIED)

    def click_on_item_button(self):
        try:
            self.item_btn.click()
        except TypeError:
            raise Exception(ExceptionText.ITEM_NOT_SPECIFIED)

    def check_that_item_button_text_is_correct(self, expected_value):
        self.check_element_text(self.item_btn, expected_value)
