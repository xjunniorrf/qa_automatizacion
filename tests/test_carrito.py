from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_agregar_producto_al_carrito(page: Page):
    # ARRANGE - usuario logueado
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # ACT - agregar la mochila
    inventory_page.add_to_cart("sauce-labs-backpack")

    # ASSERT - el carrito muestra "1"
    expect(inventory_page.cart_badge).to_have_text("1")

    # ACT - ir al carrito
    inventory_page.go_to_cart()

    # ASSERT - el producto correcto está en el carrito
    expect(page).to_have_url(CartPage.URL)
    expect(cart_page.items).to_have_count(1)
    expect(cart_page.item_name).to_have_text("Sauce Labs Backpack")
    expect(cart_page.item_quantity).to_have_text("1")
    expect(cart_page.item_price).to_have_text("$29.99")
