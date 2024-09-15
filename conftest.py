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
    login_page.open_page(LoginPageConstants.LOGIN_PAGE_URL)
    login_page.login_into_swag_labs(LoginPageConstants.VALID_USERNAME, LoginPageConstants.VALID_PASSWORD)
    yield


@pytest.fixture
def product_locators():
    def _init_locators(item_name):
        return generate_locators_for_item(item_name)
    return _init_locators


@pytest.fixture(autouse=True)
def configure_playwright_test_id_attribute(playwright):
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page, product_locators, request):
    inventory_page = InventoryPage(page)
    item_name = getattr(request, 'param', None)
    if item_name:
        inventory_page.item_locators = product_locators(item_name)
    return inventory_page
