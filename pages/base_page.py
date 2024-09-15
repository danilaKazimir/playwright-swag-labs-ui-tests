from typing import Callable
from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open_page(self, url):
        self.page.goto(url)

    def get_element_by_role(self, role, name):
        return self.page.get_by_role(role, name=name)

    def get_element_by_placeholder(self, placeholder):
        return self.page.get_by_placeholder(placeholder)

    def get_element_by_test_id(self, test_id):
        return self.page.get_by_test_id(test_id)

    def get_element_by_locator(self, locator):
        return self.page.locator(locator)

    def check_element_is_visible(self, element):
        expect(element).to_be_visible()

    def check_element_is_hidden(self, element):
        expect(element).to_be_hidden()

    def check_element_text(self, element, expected_text):
        expect(element).to_have_text(expected_text)

    def check_element_attribute(self, element, attr, exp_attr_value):
        expect(element).to_have_attribute(attr, exp_attr_value)

    def check_page_url(self, url):
        expect(self.page).to_have_url(url)

    def check_page_title(self, title):
        expect(self.page).to_have_title(title)

    def open_new_browser_tab_page_by_action(self, action: Callable[[], None]) -> None:
        """Open a new browser tab after some action and change the context to the opened tab"""
        with self.page.context.expect_page() as new_page:
            action()
        self.page = new_page.value
