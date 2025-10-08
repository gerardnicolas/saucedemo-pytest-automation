from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page1 import CheckoutPageOne
from pages.checkout_page2 import CheckoutPageTwo
from pages.checkout_page3 import CheckoutPageThree

# def test_check_out_item(browser):
#     firstname_input = (By.ID, "first-name")
#     success_header_message = (By.CLASS_NAME, "complete-header")
#
#     # Login
#     login_page = LoginPage(browser)
#     login_page.login("standard_user", "secret_sauce")
#
#     # Add Item to Cart
#     inventory_page = InventoryPage(browser)
#     inventory_page.add_product_to_cart("sauce-labs-backpack")
#
#     # Show Cart
#     inventory_page.open_cart()
#     WebDriverWait(browser, 10).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart_list"))
#     )
#     assert "cart.html" in browser.current_url
#
#     # Verify if item is in cart
#     cart_page = CartPage(browser)
#     assert cart_page._has_item("Sauce Labs Backpack"), "Cart is empty before checkout"
#     cart_items = browser.find_elements(By.CLASS_NAME, "cart_item")
#     assert len(cart_items) > 0, "Cart is empty, cannot proceed to checkout"
#     print("Before checkout click, URL:", browser.current_url)
#     print("Cart items:", len(browser.find_elements(By.CLASS_NAME, "cart_item")))
#     cart_page._click_checkout()
#
#     checkout_one = CheckoutPageOne(browser)
#     checkout_one._verify_url()
#     assert "checkout-step-one.html" in browser.current_url, f"Expected 'checkout-step-one.html' yet at {browser.current_url}."
#
#     checkout_one.fill_field((By.ID, "first-name"), "John")
#     checkout_one.fill_field((By.ID, "last-name"), "Doe")
#     checkout_one.fill_field((By.ID, "postal-code"), "1234")
#     checkout_one._click_continue()
#
#     checkout_two = CheckoutPageTwo(browser)
#     checkout_two._verify_url()
#     assert "checkout-step-two.html" in browser.current_url
#     print(f"Current URL: {browser.current_url}")
#     checkout_two._click_finish()
#
#     checkout_three = CheckoutPageThree(browser)
#     checkout_three._is_displayed(success_header_message)
#     success_message = checkout_three._get_success_message()
#
#     assert success_message == "Thank you for your order!", f"Unsuccessful checkout, header message instead returned: {success_message}"

# def test_checkout_with_missing_info(browser):
#     login_page = LoginPage(browser)
#     login_page.login("standard_user", "secret_sauce")
#
#     inventory_page = InventoryPage(browser)
#     inventory_page.add_product_to_cart("sauce-labs-backpack")
#
#     cart_page = CartPage(browser)
#     cart_page.open_cart()
#     cart_page._click_checkout()
#
#     checkout_one = CheckoutPageOne(browser)
#     checkout_one._verify_url()
#     assert "checkout-step-one.html" in browser.current_url, f"Expected 'checkout-step-one.html' yet at {browser.current_url}."
#
#     checkout_one.fill_field("John", "Doe")
#     checkout_one._continue()
#
#     print("== DIAGNOSTICS ==")
#     print("Current URL:", browser.current_url)
#     print("Error text in page_source?:", "Error: Postal Code is required" in browser.page_source)
#     matches = browser.find_elements(By.CSS_SELECTOR, "div.error-message-container h3[data-test='error']")
#     print("find_elements count for locator:", len(matches))
#     if matches:
#         print("First match text:", matches[0].text)
#     print("Page title:", browser.title)
#     print("===================")
#
#     print(f"Checking presence of element..")
#     error_message_text = checkout_one.get_error_message_text()
#     assert "Error: Postal Code is required" in error_message_text

def test_checkout_with_missing_info(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_product_to_cart("sauce-labs-backpack")

    cart_page = CartPage(browser)
    cart_page.open_cart()
    cart_page._click_checkout()

    assert "checkout-step-one.html" in browser.current_url

    first_name_input = browser.find_element(By.ID, "first-name")
    last_name_input = browser.find_element(By.ID, "last-name")
    postal_input = browser.find_element(By.ID, "postal-code")
    continue_button = browser.find_element(By.ID, "continue")

    first_name_input.send_keys("John")
    last_name_input.send_keys("Doe")

    # Confirm they contain text
    print("First name value:", first_name_input.get_attribute("value"))
    print("Last name value:", last_name_input.get_attribute("value"))
    print("Postal value:", postal_input.get_attribute("value"))

    # Click Continue
    continue_button.click()

    # Wait briefly for UI to update
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.error-message-container"))
    )

    # Print full page source snippet to check if error appeared
    page_source = browser.page_source
    print("Error message in page_source?:", "Postal Code is required" in page_source)

    # If it appears, try locating it again
    matches = browser.find_elements(By.CSS_SELECTOR, "h3[data-test='error']")
    print("Matches found:", len(matches))
    if matches:
        print("Match text:", matches[0].text)