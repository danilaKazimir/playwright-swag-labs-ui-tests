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
