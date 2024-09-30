import pytest
from pages.constants import InventoryPageConstants


class TestFooter:
    def test_twitter_link(self, login, inventory_page, cart_page, checkout_first_step_page, checkout_second_step_page,
                          faker):
        inventory_page.click_on_cart()
        cart_page.click_on_checkout_button()
        checkout_first_step_page.fill_all_field(faker.generate_first_name(), faker.generate_last_name(),
                                                faker.generate_zip_code())
        checkout_first_step_page.click_on_continue_button()
        checkout_second_step_page.open_twitter_link()

    def test_facebook_link(self, login, inventory_page, cart_page, checkout_first_step_page, checkout_second_step_page,
                           faker):
        inventory_page.click_on_cart()
        cart_page.click_on_checkout_button()
        checkout_first_step_page.fill_all_field(faker.generate_first_name(), faker.generate_last_name(),
                                                faker.generate_zip_code())
        checkout_first_step_page.click_on_continue_button()
        checkout_second_step_page.open_facebook_link()

    def test_linkedin_link(self, login, inventory_page, cart_page, checkout_first_step_page, checkout_second_step_page,
                           faker):
        inventory_page.click_on_cart()
        cart_page.click_on_checkout_button()
        checkout_first_step_page.fill_all_field(faker.generate_first_name(), faker.generate_last_name(),
                                                faker.generate_zip_code())
        checkout_first_step_page.click_on_continue_button()
        checkout_second_step_page.open_linkedin_link()

    def test_footer_copyright_text(self, login, inventory_page, cart_page, checkout_first_step_page,
                                   checkout_second_step_page,
                                   faker):
        inventory_page.click_on_cart()
        cart_page.click_on_checkout_button()
        checkout_first_step_page.fill_all_field(faker.generate_first_name(), faker.generate_last_name(),
                                                faker.generate_zip_code())
        checkout_first_step_page.click_on_continue_button()
        checkout_second_step_page.check_footer_copyright_text()


class TestBurgerMenu:
    def test_about_link(self, login, inventory_page, cart_page, checkout_first_step_page, checkout_second_step_page,
                        faker):
        inventory_page.click_on_cart()
        cart_page.click_on_checkout_button()
        checkout_first_step_page.fill_all_field(faker.generate_first_name(), faker.generate_last_name(),
                                                faker.generate_zip_code())
        checkout_first_step_page.click_on_continue_button()
        checkout_second_step_page.open_burger_menu()
        checkout_second_step_page.open_about_link()

    def test_logout_link(self, login, login_page, inventory_page, cart_page, checkout_first_step_page,
                         checkout_second_step_page,
                         faker):
        inventory_page.click_on_cart()
        cart_page.click_on_checkout_button()
        checkout_first_step_page.fill_all_field(faker.generate_first_name(), faker.generate_last_name(),
                                                faker.generate_zip_code())
        checkout_first_step_page.click_on_continue_button()
        checkout_second_step_page.open_burger_menu()
        checkout_second_step_page.logout()
        login_page.check_that_login_page_is_opened()

    def test_close_burger_menu(self, login, inventory_page, cart_page, checkout_first_step_page,
                               checkout_second_step_page,
                               faker):
        inventory_page.click_on_cart()
        cart_page.click_on_checkout_button()
        checkout_first_step_page.fill_all_field(faker.generate_first_name(), faker.generate_last_name(),
                                                faker.generate_zip_code())
        checkout_first_step_page.click_on_continue_button()
        checkout_second_step_page.open_burger_menu()
        checkout_second_step_page.close_burger_menu()

    def test_return_to_inventory_page(self, login, inventory_page, cart_page, checkout_first_step_page,
                                      checkout_second_step_page,
                                      faker):
        inventory_page.click_on_cart()
        cart_page.click_on_checkout_button()
        checkout_first_step_page.fill_all_field(faker.generate_first_name(), faker.generate_last_name(),
                                                faker.generate_zip_code())
        checkout_first_step_page.click_on_continue_button()
        checkout_second_step_page.open_burger_menu()
        checkout_second_step_page.click_on_all_item_link()
        inventory_page.check_that_inventory_page_is_opened()


@pytest.mark.parametrize('item_name', [InventoryPageConstants.ITEMS[0]], indirect=True)
class TestCancelButton:
    def test_cancel_checkout_during_buying_one_item(self, login, inventory_page, cart_page, checkout_first_step_page,
                                                    checkout_second_step_page, faker):
        inventory_page.click_on_item_button()
        inventory_page.click_on_cart()
        cart_page.click_on_checkout_button()
        checkout_first_step_page.fill_all_field(faker.generate_first_name(), faker.generate_last_name(),
                                                faker.generate_zip_code())
        checkout_first_step_page.click_on_continue_button()
        checkout_second_step_page.click_on_cancel_button()
        inventory_page.check_that_cart_badge_value_is_correct("1")
        inventory_page.check_that_item_button_text_is_correct("Remove")
