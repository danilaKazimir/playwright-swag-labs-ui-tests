class BasePageConstants:
    TWITTER_PAGE_URL = "https://x.com/saucelabs"
    TWITTER_PAGE_TITLE = "Sauce Labs (@saucelabs) / X"
    FACEBOOK_PAGE_URL = "https://www.facebook.com/saucelabs"
    FACEBOOK_PAGE_TITLE = "Sauce Labs | San Francisco CA | Facebook"
    LINKEDIN_PAGE_URL = "https://www.linkedin.com/company/sauce-labs/"
    LINKEDIN_PAGE_TITLE = "Sauce Labs | LinkedIn"
    SAUCE_LABS_COM_URL = "https://saucelabs.com/"
    SAUCE_LABS_COM_TITLE = "Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing"
    FOOTER_COPYRIGHT_TEXT = "© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"


class LoginPageConstants:
    LOGIN_PAGE_URL = "https://www.saucedemo.com/"
    LOGIN_PAGE_TITLE = "Swag Labs"
    USER_NAME_IS_NOT_FILLED_ERROR_MSG = "Epic sadface: Username is required"
    PASSWORD_IS_NOT_FILLED_ERROR_MSG = "Epic sadface: Password is required"
    INCORRECT_LOGIN_VALUES_ERROR_MSG = "Epic sadface: Username and password do not match any user in this service"
    LOCKED_USER_ERROR_MSG = "Epic sadface: Sorry, this user has been locked out."
    VALID_USERNAME = "standard_user"
    VALID_PASSWORD = "secret_sauce"


class InventoryPageConstants:
    INVENTORY_PAGE_URL = "https://www.saucedemo.com/inventory.html"
    INVENTORY_PAGE_TITLE = "Swag Labs"
    ITEMS = ("Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket",
             "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)")


class InventoryItemPageConstants:
    INVENTORY_ITEM_BASE_URL = "https://www.saucedemo.com/inventory-item.html?id="
    INVENTORY_ITEM_TITLE = "Swag Labs"


class MockApiConstants:
    GET_ALL_ITEMS = "https://swaglabsmockapi.pythonanywhere.com/mock_api/items"
