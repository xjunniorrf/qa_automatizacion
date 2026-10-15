from playwright.sync_api import Page, expect

# PENDIENTE: convertir a POM cuando creemos CheckoutPage


def test_compra_completa(page: Page):
    # ARRANGE
    page.goto("https://www.saucedemo.com/")

    # ACT - escribir credenciales y hacer clic en login
    page.locator("#user-name").fill("standard_user") # Selector, valor
    page.locator("#password").fill("secret_sauce") # el metodo fill sirve para escribir texto en campos
    page.get_by_role("button", name="Login").click() # el metodo click sirve para accionar en un boton.

    # AGREGAR PRODUCTOS AL CARRITO
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    page.locator("#add-to-cart-sauce-labs-bike-light").click()
    page.locator("#add-to-cart-sauce-labs-bolt-t-shirt").click()
    page.locator("#add-to-cart-sauce-labs-fleece-jacket").click()

    # IR A LA LISTA DEL CARRITO
    page.locator(".shopping_cart_link").click()

    # DARLE CHECKOUT
    page.locator("#checkout").click()

    # LLENAR FORMULARIO
    page.locator("#first-name").fill("Pablo")
    page.locator("#last-name").fill("Escobar")
    page.locator("#postal-code").fill("9556")
    page.locator("#continue").click()

    # Form de detalle de orden
    page.locator("#finish").click()

    #ASSERT
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(page.locator('[data-test="complete-header"]')).to_contain_text("Thank you for your order!")
