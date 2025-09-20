import pytest
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page1 import CheckoutPageOne
from pages.checkout_page2 import CheckoutPageTwo
from pages.checkout_page3 import CheckoutPageThree

def test_check_out_item(browser):
    # Login
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    # Add Item to Cart
    inventory_page = InventoryPage(browser)
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()

    # Show Cart
    cart_page = CartPage(browser)
    cart_page.click_checkout()

    print("\nDEBUG: Current URL:", browser.current_url)
    try:
        WebDriverWait(browser, 10).until(
            EC.url_contains("/checkout-step-one.html")
        )
    except TimeoutException:
        pytest.fail(f"Did not reach inventory page, current URL is: {browser.current_url}")
    print("DEBUG: Page source snippet:", browser.page_source[:500])

    # Fill-up Form
    first_name_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )
    first_name_input.send_keys("John")
    browser.find_element(By.ID, "last-name").send_keys("Doe")
    browser.find_element(By.ID, "postal-code").send_keys("1234")
    browser.find_element(By.ID, "continue").click()

    # checkout_page1 = CheckoutPageOne(browser)
    # checkout_page1.fill_up_form("John", "Doe", "1234")
    # checkout_page1.continue_form()

    # Finish Checkout
    # checkout_page2 = CheckoutPageTwo(browser)
    print("\nDEBUG: Current URL:", browser.current_url) # Must be at checkout-step-two.html
    try:
        WebDriverWait(browser, 10).until(
            EC.url_contains("/checkout-step-two.html")
        )
    except TimeoutException:
        pytest.fail(f"Did not reach inventory page, current URL is: {browser.current_url}")
    browser.find_element(By.ID, "finish").click()
    # checkout_page2.finish_form()

    # Verify Checkout
    checkout_page3 = CheckoutPageThree(browser)
    assert checkout_page3.get_success_message() == "Thank you for your order!"



