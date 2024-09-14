from pages.login_page import LoginPage
import pytest

VALID_LOGIN_DATA = {
    "username": "standard_user",
    "password": "secret_sauce"
}
INVALID_LOGIN_DATA = (
    ("", ""),
    ("", "secret_sauce"),
    ("standard_user", ""),
    ("invalid_login", "secret_sauce"),
    ("standard_user", "invalid_password"),
    ("invalid_login", "invalid_password)"),
    ("locked_out_user", "secret_sauce")
)
ERROR_MESSAGES = {
    "Username isn't filled": "Epic sadface: Username is required",
    "Password isn't filled": "Epic sadface: Password is required",
    "Incorrect login values": "Epic sadface: Username and password do not match any user in this service",
    "Locked user": "Epic sadface: Sorry, this user has been locked out."
}


def test_successful_login_into_swag_labs(login_page):
    login_page.open_page(LoginPage.URL)
    login_page.login_into_swag_labs(VALID_LOGIN_DATA["username"], VALID_LOGIN_DATA["password"])


@pytest.mark.parametrize("username, password", INVALID_LOGIN_DATA)
def test_unsuccessful_login_into_swag_labs(login_page, username, password):
    if username == "":
        expected_error = ERROR_MESSAGES["Username isn't filled"]
    elif password == "" and username != "":
        expected_error = ERROR_MESSAGES["Password isn't filled"]
    elif username == "locked_out_user" and password == "secret_sauce":
        expected_error = ERROR_MESSAGES["Locked user"]
    else:
        expected_error = ERROR_MESSAGES["Incorrect login values"]
    login_page.open_page(LoginPage.URL)
    login_page.login_into_swag_labs(username, password, is_success_login=False, error_text=expected_error)
