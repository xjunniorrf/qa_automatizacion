from playwright.sync_api import Page

class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        self.page = page
        # LOCATORS
        self.title = page.locator('[data-test="title"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')

    # ACCIONES
    def add_to_cart(self, product: str):
        self.page.locator(f'[data-test="add-to-cart-{product}"]').click()

    def go_to_cart(self):
        self.cart_link.click()