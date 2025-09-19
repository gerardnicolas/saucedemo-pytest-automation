# login, click add to cart, check cart, if item is in cart assert
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_item_to_cart(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()

    cart = CartPage(browser)
    assert cart.has_item("Sauce Labs Backpack")



