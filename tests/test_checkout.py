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