import pytest
from playwright.sync_api import Page


@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 1080, 'width': 1920})
    yield page


@pytest.fixture(autouse=True)
def configure_playwright_test_id_attribute(playwright):
    playwright.selectors.set_test_id_attribute("data-test")
