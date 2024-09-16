import pytest
from pages.constants import InventoryPageConstants


class TestFooter:
    def test_twitter_link(self, inventory_page, login):
        inventory_page.open_twitter_link()

    def test_facebook_link(self, inventory_page, login):
        inventory_page.open_facebook_link()

    def test_linkedin_link(self, inventory_page, login):
        inventory_page.open_linkedin_link()

    def test_footer_copyright_text(self, inventory_page, login):
        inventory_page.check_footer_copyright_text()


class TestBurgerMenu:
    def test_about_link(self, inventory_page, login):
        inventory_page.open_burger_menu()
        inventory_page.open_about_link()

    def test_logout_link(self, inventory_page, login_page, login):
        inventory_page.open_burger_menu()
        inventory_page.logout()
        login_page.check_that_login_page_is_opened()

    def test_close_burger_menu(self, inventory_page, login):
        inventory_page.open_burger_menu()
        inventory_page.close_burger_menu()


@pytest.mark.parametrize('item_name', InventoryPageConstants.ITEMS, indirect=True)
class TestItems:
    def test_check_item_values(self, inventory_page, login):
        inventory_page.check_item_values()

    def test_open_item_page_by_clicking_on_item_name_link(self, inventory_page, inventory_item_page, login):
        inventory_page.click_on_item_name_link()
        inventory_item_page.check_that_inventory_item_page_is_opened()

    def test_open_item_page_by_clicking_on_item_image_link(self, inventory_page, inventory_item_page, login):
        inventory_page.click_on_item_image_link()
        inventory_item_page.check_that_inventory_item_page_is_opened()

    def test_add_and_remove_item_from_cart(self, inventory_page, login):
        inventory_page.click_on_item_button()
        inventory_page.check_that_item_button_text_is_correct("Remove")
        inventory_page.check_that_cart_badge_value_is_correct("1")
        inventory_page.click_on_item_button()
        inventory_page.check_that_item_button_text_is_correct("Add to cart")
        inventory_page.check_that_cart_badge_is_not_displayed()

    def test_check_the_added_item_into_cart_status_after_re_login(self, inventory_page, login):
        inventory_page.click_on_item_button()
        inventory_page.open_burger_menu()
        inventory_page.logout()
        login()
        inventory_page.check_that_item_button_text_is_correct("Remove")
        inventory_page.check_that_cart_badge_value_is_correct("1")
