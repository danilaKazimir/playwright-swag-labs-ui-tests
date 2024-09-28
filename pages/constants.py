class BasePageConstants:
    TWITTER_PAGE_URL = "https://x.com/saucelabs"
    TWITTER_PAGE_TITLE = "Sauce Labs (@saucelabs) / X"
    FACEBOOK_PAGE_URL = "https://www.facebook.com/saucelabs"
    FACEBOOK_PAGE_TITLE = "Sauce Labs | Facebook"
    LINKEDIN_PAGE_URL = "https://www.linkedin.com/company/sauce-labs/"
    LINKEDIN_PAGE_TITLE = "Sauce Labs | LinkedIn"
    SAUCE_LABS_COM_URL = "https://saucelabs.com/"
    SAUCE_LABS_COM_TITLE = "Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing"
    FOOTER_COPYRIGHT_TEXT = "© 2024 Sauce Labs. All Rights Reserved. Terms of Service | Privacy Policy"
    SWAG_LABS_LOGO = "Swag Labs"


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
    INVENTORY_PAGE_HEADER = "Products"
    ITEMS = ("Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket",
             "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)")


class InventoryItemPageConstants:
    INVENTORY_ITEM_BASE_URL = "https://www.saucedemo.com/inventory-item.html?id="
    INVENTORY_ITEM_TITLE = "Swag Labs"


class CartPageConstants:
    CART_PAGE_URL = "https://www.saucedemo.com/cart.html"
    CART_PAGE_TITLE = "Swag Labs"
    CART_PAGE_HEADER = "Your Cart"


class CheckoutFirstStepConstants:
    CHECKOUT_FIRST_STEP_URL = "https://www.saucedemo.com/checkout-step-one.html"
    CHECKOUT_FIRST_STEP_TITLE = "Swag Labs"
    CHECKOUT_FIRST_STEP_HEADER = "Checkout: Your Information"


class CheckoutSecondStepConstants:
    CHECKOUT_SECOND_STEP_URL = "https://www.saucedemo.com/checkout-step-two.html"
    CHECKOUT_SECOND_STEP_TITLE = "Swag Labs"
    CHECKOUT_SECOND_STEP_HEADER = "Checkout: Overview"
    SAUCE_CART = "SauceCard #31337"
    SHIPPING_OPTION = "Free Pony Express Delivery!"
    TAX_PERCENT = 8


class CheckoutFinishConstants:
    CHECKOUT_FINISH_URL = "https://www.saucedemo.com/checkout-complete.html"
    CHECKOUT_FINISH_TITLE = "Swag Labs"
    CHECKOUT_FINISH_HEADER = "Checkout: Complete!"
    COMPLETE_HEADER = "Thank you for your order!"
    COMPLETE_TEXT = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"


class MockApiConstants:
    GET_ALL_ITEMS = "https://swaglabsmockapi.pythonanywhere.com/mock_api/items"
