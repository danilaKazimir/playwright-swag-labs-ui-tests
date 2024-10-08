import pytest
from pages.constants import InventoryPageConstants


@pytest.mark.parametrize('item_name', [InventoryPageConstants.ITEMS[0]], indirect=True)
class TestFooter:
    def test_twitter_link(self, inventory_page, inventory_item_page, login):
        inventory_page.click_on_item_name_link()
        inventory_item_page.open_twitter_link()

    def test_facebook_link(self, inventory_page, inventory_item_page, login):
        inventory_page.click_on_item_name_link()
        inventory_item_page.open_facebook_link()

    def test_linkedin_link(self, inventory_page, inventory_item_page, login):
        inventory_page.click_on_item_name_link()
        inventory_item_page.open_linkedin_link()

    def test_footer_copyright_text(self, inventory_page, inventory_item_page, login):
        inventory_page.click_on_item_name_link()
        inventory_item_page.check_footer_copyright_text()


@pytest.mark.parametrize('item_name', [InventoryPageConstants.ITEMS[0]], indirect=True)
class TestBurgerMenu:
    def test_about_link(self, inventory_page, inventory_item_page, login):
        inventory_page.click_on_item_name_link()
        inventory_item_page.open_burger_menu()
        inventory_item_page.open_about_link()

    def test_logout_link(self, inventory_page, inventory_item_page, login_page, login):
        inventory_page.click_on_item_name_link()
        inventory_item_page.open_burger_menu()
        inventory_item_page.logout()
        login_page.check_that_login_page_is_opened()

    def test_close_burger_menu(self, inventory_page, inventory_item_page, login):
        inventory_page.click_on_item_name_link()
        inventory_item_page.open_burger_menu()
        inventory_item_page.close_burger_menu()

    def test_return_to_inventory_page(self, inventory_page, inventory_item_page, login):
        inventory_page.click_on_item_name_link()
        inventory_item_page.open_burger_menu()
        inventory_item_page.click_on_all_item_link()
        inventory_page.check_that_inventory_page_is_opened()


@pytest.mark.parametrize('item_name', [InventoryPageConstants.ITEMS[0]], indirect=True)
class TestBackToProductLink:
    def test_return_to_inventory_page_using_link(self, inventory_page, inventory_item_page, login):
        inventory_page.click_on_item_name_link()
        inventory_item_page.click_on_back_to_products_link()
        inventory_page.check_that_inventory_page_is_opened()


@pytest.mark.parametrize('item_name', InventoryPageConstants.ITEMS, indirect=True)
class TestItem:
    def test_add_and_remove_item_from_cart(self, inventory_page, inventory_item_page, login):
        inventory_page.click_on_item_name_link()
        inventory_item_page.check_that_item_button_text_is_correct("Add to cart")
        inventory_item_page.check_that_cart_badge_is_not_displayed()
        inventory_item_page.click_on_item_button()
        inventory_item_page.check_that_item_button_text_is_correct("Remove")
        inventory_item_page.check_that_cart_badge_value_is_correct("1")
        inventory_item_page.click_on_item_button()
        inventory_item_page.check_that_item_button_text_is_correct("Add to cart")
        inventory_item_page.check_that_cart_badge_is_not_displayed()

    def test_check_the_added_item_into_cart_status_after_re_login(self, inventory_page, inventory_item_page, login):
        inventory_page.click_on_item_name_link()
        inventory_item_page.click_on_item_button()
        inventory_item_page.open_burger_menu()
        inventory_item_page.logout()
        login()
        inventory_page.click_on_item_name_link()
        inventory_item_page.check_that_item_button_text_is_correct("Remove")
        inventory_item_page.check_that_cart_badge_value_is_correct("1")
