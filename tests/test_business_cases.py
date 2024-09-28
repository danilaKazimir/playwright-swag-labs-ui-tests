import pytest
from pages.constants import InventoryPageConstants


@pytest.mark.parametrize('item_name', InventoryPageConstants.ITEMS, indirect=True)
class TestBuyOneItem:
    def test_buy_one_item_from_the_inventory_page(self, login, inventory_page, cart_page, checkout_first_step_page,
                                                  checkout_second_step_page, checkout_finish_page):
        inventory_page.click_on_item_button()
        inventory_page.check_that_cart_badge_value_is_correct("1")
        inventory_page.click_on_cart()

        cart_page.check_that_cart_page_is_opened()
        cart_page.check_that_cart_badge_value_is_correct("1")
        cart_page.check_item_values()
        cart_page.click_on_checkout_button()

        checkout_first_step_page.check_that_checkout_first_step_page_is_opened()
        checkout_first_step_page.check_that_cart_badge_value_is_correct("1")
        checkout_first_step_page.fill_first_name_input("Test First Name")
        checkout_first_step_page.fill_last_name_input("Test Last Name")
        checkout_first_step_page.fill_zip_code_input("40202")
        checkout_first_step_page.click_on_continue_button()

        checkout_second_step_page.check_that_checkout_second_step_is_opened()
        checkout_second_step_page.check_that_cart_badge_value_is_correct("1")
        checkout_second_step_page.check_that_payment_information_is_correct()
        checkout_second_step_page.check_that_shipping_information_is_correct()
        checkout_second_step_page.check_that_item_total_label_is_correct()
        checkout_second_step_page.check_that_item_tax_label_is_correct()
        checkout_second_step_page.check_that_price_total_value_is_correct()
        checkout_second_step_page.click_on_finish_button()

        checkout_finish_page.check_that_checkout_finish_page_is_opened()
        checkout_finish_page.check_that_cart_badge_is_not_displayed()
        checkout_finish_page.check_that_pony_express_image_is_displayed()
        checkout_finish_page.check_that_complete_header_text_is_correct()
        checkout_finish_page.check_that_complete_text_is_correct()
        checkout_finish_page.click_on_back_home_button()

        inventory_page.check_that_inventory_page_is_opened()
        inventory_page.check_that_cart_badge_is_not_displayed()

    def test_buy_one_item_from_the_inventory_item_page(self, login, inventory_page, inventory_item_page, cart_page,
                                                       checkout_first_step_page, checkout_second_step_page,
                                                       checkout_finish_page):
        inventory_page.click_on_item_name_link()

        inventory_item_page.check_that_inventory_item_page_is_opened()
        inventory_item_page.click_on_item_button()
        inventory_item_page.check_that_cart_badge_value_is_correct("1")
        inventory_item_page.click_on_cart()

        cart_page.check_that_cart_page_is_opened()
        cart_page.check_that_cart_badge_value_is_correct("1")
        cart_page.check_item_values()
        cart_page.click_on_checkout_button()

        checkout_first_step_page.check_that_checkout_first_step_page_is_opened()
        checkout_first_step_page.check_that_cart_badge_value_is_correct("1")
        checkout_first_step_page.fill_first_name_input("Test First Name")
        checkout_first_step_page.fill_last_name_input("Test Last Name")
        checkout_first_step_page.fill_zip_code_input("40202")
        checkout_first_step_page.click_on_continue_button()

        checkout_second_step_page.check_that_checkout_second_step_is_opened()
        checkout_second_step_page.check_that_cart_badge_value_is_correct("1")
        checkout_second_step_page.check_that_payment_information_is_correct()
        checkout_second_step_page.check_that_shipping_information_is_correct()
        checkout_second_step_page.check_that_item_total_label_is_correct()
        checkout_second_step_page.check_that_item_tax_label_is_correct()
        checkout_second_step_page.check_that_price_total_value_is_correct()
        checkout_second_step_page.click_on_finish_button()

        checkout_finish_page.check_that_checkout_finish_page_is_opened()
        checkout_finish_page.check_that_cart_badge_is_not_displayed()
        checkout_finish_page.check_that_pony_express_image_is_displayed()
        checkout_finish_page.check_that_complete_header_text_is_correct()
        checkout_finish_page.check_that_complete_text_is_correct()
        checkout_finish_page.click_on_back_home_button()

        inventory_page.check_that_inventory_page_is_opened()
        inventory_page.check_that_cart_badge_is_not_displayed()
