from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def get_element_by_role(self, role, name):
        return self.page.get_by_role(role, name=name)

    def get_element_by_placeholder(self, placeholder):
        return self.page.get_by_placeholder(placeholder)

    def open_page(self, url):
        self.page.goto(url)
