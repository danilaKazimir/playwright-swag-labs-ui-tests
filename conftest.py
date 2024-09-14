import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.constants import LoginPageConstants


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


@pytest.fixture(autouse=True)
def configure_playwright_test_id_attribute(playwright):
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)
