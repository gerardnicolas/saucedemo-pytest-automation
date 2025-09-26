from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page1 import CheckoutPageOne
from pages.checkout_page2 import CheckoutPageTwo
from pages.checkout_page3 import CheckoutPageThree

def test_check_out_item(browser):
    firstname_input = (By.ID, "first-name")
    success_header_message = (By.CLASS_NAME, "complete-header")

    # Login
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    # Add Item to Cart
    inventory_page = InventoryPage(browser)
    inventory_page.add_product_to_cart("sauce-labs-backpack")

    # Show Cart
    inventory_page.open_cart()
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart_list"))
    )
    assert "cart.html" in browser.current_url

    # Verify if item is in cart
    cart_page = CartPage(browser)
    assert cart_page._has_item("Sauce Labs Backpack"), "Cart is empty before checkout"
    cart_page._click_checkout()

    checkout_one = CheckoutPageOne(browser)
    checkout_one._verify_url()
    assert "checkout-step-one.html" in browser.current_url, f"Expected 'checkout-step-one.html' yet at {browser.current_url}."
    print(f"Current URL: {browser.current_url}")

    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("John")
    assert checkout_one.is_displayed(firstname_input)
    browser.find_element(By.ID, "last-name").send_keys("Doe")
    browser.find_element(By.ID, "postal-code").send_keys("1234")
    checkout_one._click_continue()

    checkout_two = CheckoutPageTwo(browser)
    checkout_two._verify_url()
    assert "checkout-step-two.html" in browser.current_url
    print(f"Current URL: {browser.current_url}")
    checkout_two._click_finish()

    checkout_three = CheckoutPageThree(browser)
    checkout_three._is_displayed(success_header_message)
    success_message = checkout_three._get_success_message()

    assert success_message == "Thank you for your order!", f"Unsuccessful checkout, header message instead returned: {success_message}"