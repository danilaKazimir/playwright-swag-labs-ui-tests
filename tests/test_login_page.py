from pages.constants import LoginPageConstants
import pytest


class TestSuccessfulLogin:
    def test_successful_login_into_swag_labs(self, login_page, inventory_page):
        login_page.open_page(LoginPageConstants.LOGIN_PAGE_URL)
        login_page.login_into_swag_labs(LoginPageConstants.VALID_USERNAME, LoginPageConstants.VALID_PASSWORD)
        inventory_page.check_that_inventory_page_is_opened()


class TestUnsuccessfulLogin:
    INVALID_LOGIN_DATA = (
        ("", ""),
        ("", "secret_sauce"),
        ("standard_user", ""),
        ("invalid_login", "secret_sauce"),
        ("standard_user", "invalid_password"),
        ("invalid_login", "invalid_password)"),
        ("locked_out_user", "secret_sauce")
    )

    @pytest.mark.parametrize("username, password", INVALID_LOGIN_DATA)
    def test_unsuccessful_login_into_swag_labs(self, login_page, username, password):
        if username == "":
            expected_error = LoginPageConstants.USER_NAME_IS_NOT_FILLED_ERROR_MSG
        elif password == "" and username != "":
            expected_error = LoginPageConstants.PASSWORD_IS_NOT_FILLED_ERROR_MSG
        elif username == "locked_out_user" and password == "secret_sauce":
            expected_error = LoginPageConstants.LOCKED_USER_ERROR_MSG
        else:
            expected_error = LoginPageConstants.INCORRECT_LOGIN_VALUES_ERROR_MSG
        login_page.open_page(LoginPageConstants.LOGIN_PAGE_URL)
        login_page.login_into_swag_labs(username, password, is_success_login=False, error_text=expected_error)
