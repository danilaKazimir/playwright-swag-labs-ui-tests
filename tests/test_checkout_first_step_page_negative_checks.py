import pytest
from pages.constants import InventoryPageConstants, CheckoutFirstStepConstants


@pytest.mark.parametrize('item_name', [InventoryPageConstants.ITEMS[0]], indirect=True)
class TestYourInformationErrorMessage:
    def test_first_name_field_is_not_filled(self, login, inventory_page, cart_page, checkout_first_step_page, faker):
        inventory_page.click_on_item_button()
        inventory_page.click_on_cart()

        cart_page.click_on_checkout_button()

        checkout_first_step_page.fill_last_name_input(faker.generate_last_name())
        checkout_first_step_page.fill_zip_code_input(faker.generate_zip_code())
        checkout_first_step_page.click_on_continue_button()
        checkout_first_step_page.check_that_field_error_icons_are_displayed()
        checkout_first_step_page.check_that_error_message_displayed_correctly(
            CheckoutFirstStepConstants.FIRST_NAME_ERROR)
        checkout_first_step_page.click_on_error_message_close_button()
        checkout_first_step_page.check_that_field_error_icons_are_not_visible()
        checkout_first_step_page.check_that_error_message_is_not_visible()

    def test_last_name_field_is_not_filled(self, login, inventory_page, cart_page, checkout_first_step_page, faker):
        inventory_page.click_on_item_button()
        inventory_page.click_on_cart()

        cart_page.click_on_checkout_button()

        checkout_first_step_page.fill_first_name_input(faker.generate_first_name())
        checkout_first_step_page.fill_zip_code_input(faker.generate_zip_code())
        checkout_first_step_page.click_on_continue_button()
        checkout_first_step_page.check_that_field_error_icons_are_displayed()
        checkout_first_step_page.check_that_error_message_displayed_correctly(
            CheckoutFirstStepConstants.LAST_NAME_ERROR)
        checkout_first_step_page.click_on_error_message_close_button()
        checkout_first_step_page.check_that_field_error_icons_are_not_visible()
        checkout_first_step_page.check_that_error_message_is_not_visible()

    def test_zip_code_field_is_not_filled(self, login, inventory_page, cart_page, checkout_first_step_page, faker):
        inventory_page.click_on_item_button()
        inventory_page.click_on_cart()

        cart_page.click_on_checkout_button()

        checkout_first_step_page.fill_first_name_input(faker.generate_first_name())
        checkout_first_step_page.fill_last_name_input(faker.generate_last_name())
        checkout_first_step_page.click_on_continue_button()
        checkout_first_step_page.check_that_field_error_icons_are_displayed()
        checkout_first_step_page.check_that_error_message_displayed_correctly(
            CheckoutFirstStepConstants.ZIP_CODE_ERROR)
        checkout_first_step_page.click_on_error_message_close_button()
        checkout_first_step_page.check_that_field_error_icons_are_not_visible()
        checkout_first_step_page.check_that_error_message_is_not_visible()
