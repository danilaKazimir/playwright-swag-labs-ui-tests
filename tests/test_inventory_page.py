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


class TestItems:
    @pytest.mark.parametrize('item_name', InventoryPageConstants.ITEMS, indirect=True)
    def test_check_item_values(self, inventory_page, login):
        inventory_page.check_item_values()

    @pytest.mark.parametrize('item_name', InventoryPageConstants.ITEMS, indirect=True)
    def test_open_item_page_by_clicking_on_item_name_link(self, inventory_page, inventory_item_page, login):
        inventory_page.click_on_item_name_link()
        inventory_item_page.check_that_inventory_item_page_is_opened()

    @pytest.mark.parametrize('item_name', InventoryPageConstants.ITEMS, indirect=True)
    def test_open_item_page_by_clicking_on_item_image_link(self, inventory_page, inventory_item_page, login):
        inventory_page.click_on_item_image_link()
        inventory_item_page.check_that_inventory_item_page_is_opened()
