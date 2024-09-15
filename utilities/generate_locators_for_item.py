def generate_locators_for_item(item):
    item_name = f"//div[text() = '{item}']"
    item_desc = f"{item_name}/ancestor::div[contains(@class, 'inventory_item')]//div[@data-test='inventory-item-desc']"
    item_price = f"{item_name}/ancestor::div[contains(@class, 'inventory_item')]//div[@data-test='inventory-item-price']"
    item_img = f"{item_name}/ancestor::div[contains(@class, 'inventory_item')]//img"
    item_button = f"{item_name}/ancestor::div[contains(@class, 'inventory_item')]//button"

    item_locators = {
        "name": item_name,
        "description": item_desc,
        "price": item_price,
        "image": item_img,
        "button": item_button
    }

    return item_locators
