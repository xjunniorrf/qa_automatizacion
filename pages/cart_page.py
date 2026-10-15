from playwright.sync_api import Page


class CartPage:
    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page):
        self.page = page
        # LOCATORS
        self.items = page.locator('[data-test="inventory-item"]')
        self.item_name = page.locator('[data-test="inventory-item-name"]')
        self.item_quantity = page.locator('[data-test="item-quantity"]')
        self.item_price = page.locator('[data-test="inventory-item-price"]')
        self.checkout_button = page.get_by_role("button", name="Checkout")

    # ACCIONES
    def checkout(self):
        self.checkout_button.click()
