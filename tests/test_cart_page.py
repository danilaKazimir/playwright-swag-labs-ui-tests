import pytest
from pages.constants import InventoryPageConstants


@pytest.mark.parametrize('item_name', [InventoryPageConstants.ITEMS[0]], indirect=True)
class TestFooter:
    def test_twitter_link(self, inventory_page, cart_page, login):
        inventory_page.click_on_cart()
        cart_page.open_twitter_link()

    def test_facebook_link(self, inventory_page, cart_page, login):
        inventory_page.click_on_cart()
        cart_page.open_facebook_link()

    def test_linkedin_link(self, inventory_page, cart_page, login):
        inventory_page.click_on_cart()
        cart_page.open_linkedin_link()

    def test_footer_copyright_text(self, inventory_page, cart_page, login):
        inventory_page.click_on_cart()
        cart_page.check_footer_copyright_text()


@pytest.mark.parametrize('item_name', [InventoryPageConstants.ITEMS[0]], indirect=True)
class TestBurgerMenu:
    def test_about_link(self, inventory_page, cart_page, login):
        inventory_page.click_on_item_name_link()
        cart_page.open_burger_menu()
        cart_page.open_about_link()

    def test_logout_link(self, inventory_page, cart_page, login_page, login):
        inventory_page.click_on_item_name_link()
        cart_page.open_burger_menu()
        cart_page.logout()
        login_page.check_that_login_page_is_opened()

    def test_close_burger_menu(self, inventory_page, cart_page, login):
        inventory_page.click_on_item_name_link()
        cart_page.open_burger_menu()
        cart_page.close_burger_menu()

    def test_return_to_inventory_page(self, inventory_page, cart_page, login):
        inventory_page.click_on_item_name_link()
        cart_page.open_burger_menu()
        cart_page.click_on_all_item_link()
        inventory_page.check_that_inventory_page_is_opened()


class TestBackToInventoryPage:
    def test_back_to_inventory_page_when_cart_is_empty(self, inventory_page, cart_page, login):
        inventory_page.click_on_cart()
        cart_page.check_that_cart_page_is_opened()
        cart_page.check_that_cart_badge_is_not_displayed()
        cart_page.click_on_continue_shopping_btn()
        inventory_page.check_that_inventory_page_is_opened()
        inventory_page.check_that_cart_badge_is_not_displayed()

    @pytest.mark.parametrize('item_name', [InventoryPageConstants.ITEMS[0]], indirect=True)
    def test_back_to_inventory_page_when_cart_is_not_empty(self, inventory_page, cart_page, login):
        inventory_page.click_on_item_button()
        inventory_page.click_on_cart()
        cart_page.check_that_cart_page_is_opened()
        cart_page.click_on_continue_shopping_btn()
        inventory_page.check_that_inventory_page_is_opened()
        inventory_page.check_that_cart_badge_value_is_correct("1")


@pytest.mark.parametrize('item_name', InventoryPageConstants.ITEMS, indirect=True)
class TestItem:
    def test_check_item_values(self, inventory_page, cart_page, login):
        inventory_page.click_on_item_button()
        inventory_page.click_on_cart()
        cart_page.check_that_cart_page_is_opened()
        cart_page.check_item_values()
        cart_page.check_that_cart_badge_value_is_correct("1")

    def test_remove_from_cart(self, inventory_page, cart_page, login):
        inventory_page.click_on_item_button()
        inventory_page.click_on_cart()
        cart_page.check_that_cart_page_is_opened()
        cart_page.click_on_item_remove_button()
        cart_page.check_that_cart_badge_is_not_displayed()
        cart_page.check_that_item_is_not_displayed()


@pytest.mark.parametrize('item_name', [InventoryPageConstants.ITEMS[0]], indirect=True)
class TestContinueCheckout:
    def test_continue_checkout(self, inventory_page, cart_page, checkout_first_step_page, login):
        inventory_page.click_on_item_button()
        inventory_page.click_on_cart()
        cart_page.check_that_cart_page_is_opened()
        cart_page.click_on_checkout_button()
        checkout_first_step_page.check_that_checkout_first_step_page_is_opened()
