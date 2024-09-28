import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.inventory_item_page import InventoryItemPage
from pages.cart_page import CartPage
from pages.constants import LoginPageConstants, MockApiConstants
from pages.checkout_first_step_page import CheckoutFirstStepPage
from pages.checkout_second_step_page import CheckoutSecondStepPage
from pages.checkout_finish_page import CheckoutFinishPage


@pytest.fixture
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 1080, 'width': 1920})
    yield page


@pytest.fixture
def login(login_page):
    """Login into the Swag Labs app"""

    def login_into_app():
        login_page.open_page(LoginPageConstants.LOGIN_PAGE_URL)
        login_page.login_into_swag_labs(LoginPageConstants.VALID_USERNAME, LoginPageConstants.VALID_PASSWORD)

    login_into_app()
    return login_into_app


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
def item_name(request):
    """Fixture to provide item_name parameter for inventory_page and inventory_item_page fixtures"""
    return getattr(request, 'param', None)


@pytest.fixture
def inventory_page(page, item_locators, item_name):
    """Initialization of the inventory page."""
    inventory_page = InventoryPage(page)
    if item_name:
        inventory_page.item_locators = item_locators(item_name)
        inventory_page.expected_item_values = (
            inventory_page.get_single_item_values_from_mock_api(MockApiConstants.GET_ALL_ITEMS, item_name)
        )
    return inventory_page


@pytest.fixture
def inventory_item_page(page, item_name):
    """Initialization of the inventory item page."""
    inventory_item_page = InventoryItemPage(page)
    if item_name:
        inventory_item_page.expected_item_values = (
            inventory_item_page.get_single_item_values_from_mock_api(MockApiConstants.GET_ALL_ITEMS, item_name)
        )
    return inventory_item_page


@pytest.fixture
def cart_page(page, item_name):
    """Initialization of the cart page"""
    cart_page = CartPage(page)
    if item_name:
        cart_page.expected_item_values = (
            cart_page.get_single_item_values_from_mock_api(MockApiConstants.GET_ALL_ITEMS, item_name)
        )
    return cart_page


@pytest.fixture
def checkout_first_step_page(page):
    """Initialization of the checkout first step page"""
    return CheckoutFirstStepPage(page)


@pytest.fixture
def checkout_second_step_page(page):
    """Initialization of the checkout second step page"""
    return CheckoutSecondStepPage(page)


@pytest.fixture
def checkout_finish_page(page):
    """Initialization of the checkout finish page"""
    return CheckoutFinishPage(page)
