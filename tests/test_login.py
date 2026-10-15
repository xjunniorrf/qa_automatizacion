from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_login_exitoso(page: Page):
    # ARRANGE - estar en la pagina de login
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    login_page.navigate()

    # ACT
    login_page.login("standard_user","secret_sauce")

    # ASSERT
    expect(page).to_have_url(InventoryPage.URL)
    expect(inventory_page.title).to_have_text("Products")


def test_login_credenciales_incorrectas(page: Page):
    # ARRANGE
    login_page = LoginPage(page)
    login_page.navigate()

    # ACT
    login_page.login("usuario_falso", "clave123")

    # ASSERT
    expect(login_page.error_message).to_contain_text("Username and password do not match")
