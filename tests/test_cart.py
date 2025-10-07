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
    assert cart._has_item("Sauce Labs Backpack")

def test_add_multiple_items_to_cart(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.add_product_to_cart("sauce-labs-bike-light")
    inventory_page.add_product_to_cart("sauce-labs-bolt-t-shirt")

    cart = CartPage(browser)
    cart.open_cart()
    assert cart._has_item("Sauce Labs Backpack")
    assert cart._has_item("Sauce Labs Bike Light")
    assert cart._has_item("Sauce Labs Bolt T-Shirt")