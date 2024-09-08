from pages.login_page import LoginPage


def test_successful_login_into_swag_labs(page):
    login_page = LoginPage(page)
    login_page.open_page(LoginPage.URL)
    login_page.login_into_swag_labs()

