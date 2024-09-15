import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.constants import LoginPageConstants
from utilities.generate_locators_for_item import generate_locators_for_item


@pytest.fixture
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 1080, 'width': 1920})
    yield page


@pytest.fixture
def login(login_page):
    """Login into the Swag Labs app"""
    login_page.open_page(LoginPageConstants.LOGIN_PAGE_URL)
    login_page.login_into_swag_labs(LoginPageConstants.VALID_USERNAME, LoginPageConstants.VALID_PASSWORD)
    yield


@pytest.fixture
def item_locators():
    """Initialization of item locators. The main idea is that all item value locators can be found similarly,
    so I don't need to use a unique locator for specific item. This method finds all needed item locators by item name."""
    def _init_locators(item):
        item_name = f"//div[text() = '{item}']"
        item_desc = f"{item_name}/ancestor::div[contains(@class, 'inventory_item')]//div[@data-test='inventory-item-desc']"
        item_price = f"{item_name}/ancestor::div[contains(@class, 'inventory_item')]//div[@data-test='inventory-item-price']"
        item_img = f"{item_name}/ancestor::div[contains(@class, 'inventory_item')]//img"
        item_button = f"{item_name}/ancestor::div[contains(@class, 'inventory_item')]//button"

        item_locators = {
            "name": item_name,
            "description": item_desc,
            "price": item_price,
            "image": item_img,
            "button": item_button
        }
        return item_locators
    return _init_locators


@pytest.fixture(autouse=True)
def configure_playwright_test_id_attribute(playwright):
    """Set test id attribute"""
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture
def login_page(page):
    """Initialization of the login page"""
    return LoginPage(page)


@pytest.fixture
def inventory_page(page, item_locators, request):
    """Initialization of the inventory page"""
    inventory_page = InventoryPage(page)
    item_name = getattr(request, 'param', None)
    if item_name:
        inventory_page.item_locators = item_locators(item_name)
    return inventory_page
