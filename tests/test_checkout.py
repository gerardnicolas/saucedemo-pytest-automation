from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page1 import CheckoutPageOne
from pages.checkout_page2 import CheckoutPageTwo
from pages.checkout_page3 import CheckoutPageThree

def test_check_out_item(browser):
    firstname_input = (By.ID, "first-name")
    lastname_input = (By.ID, "last-name")
    postalcode_input = (By.ID, "postal-code")

    # Login
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    # Add Item to Cart
    inventory_page = InventoryPage(browser)
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()

    # Show Cart
    cart_page = CartPage(browser)
    assert cart_page._has_item("Sauce Labs Backpack"), "Cart is empty before checkout"
    cart_page._click_checkout()

    checkout_one = CheckoutPageOne(browser)
    checkout_one._verify_url()
    assert "checkout-step-one.html" in browser.current_url
    print(f"Current URL: {browser.current_url}")
    checkout_one.fill_input_field(firstname_input, "John")
    checkout_one.fill_input_field(lastname_input, "Doe")
    checkout_one.fill_input_field(postalcode_input, 1234)
    checkout_one._click_continue()

    checkout_two = CheckoutPageTwo(browser)
    assert "checkout-step-two.html" in browser.current_url
    checkout_two._verify_url()
    print(f"Current URL: {browser.current_url}")
    checkout_two._click_finish()

    checkout_three = CheckoutPageThree(browser)
    success_message = checkout_three._get_success_message()

    assert success_message == "Thank you for your order!", f"Unsuccessful checkout, header message instead returned: {success_message}"