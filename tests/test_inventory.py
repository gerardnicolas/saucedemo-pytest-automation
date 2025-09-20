import pytest
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_verify_products_load(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item"))
    )

    products = browser.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) == 6, f"Expected 6 products, but found {len(products)}"

def test_sort_products_by_name(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item"))
    )

    sort_dropdown = Select(browser.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_value("az")

    product_elements = browser.find_elements(By.CLASS_NAME, "inventory_item_name")
    names = [el.text for el in product_elements]

    expected_names = sorted(names)
    assert names == expected_names, "Products are not sorted A->Z correctly"

    sort_dropdown = Select(browser.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_value("za")

    product_elements = browser.find_elements(By.CLASS_NAME, "inventory_item_name")
    names = [el.text for el in product_elements]

    expected_names = sorted(names, reverse=True)
    assert names == expected_names, "Products are not sorted Z-> correctly"

def test_sort_products_by_price(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item"))
    )

    sort_dropdown = Select(browser.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_value("lohi")

    # Get product prices
    product_prices = browser.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = [float(el.text.replace("$", "")) for el in product_prices]

    expected_prices = sorted(prices)
    assert prices == expected_prices, f"Product prices are not sorted from low to high"

    sort_dropdown = Select(browser.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_value("hilo")

    product_prices = browser.find_elements(By.CLASS_NAME, "inventory_item_price")
    prices = [float(el.text.replace("$", "")) for el in product_prices]

    expected_prices = sorted(prices, reverse=True)
    assert prices == expected_prices, f"Product prices are not sorted from high to low"

def test_add_item_to_cart(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_product_to_cart("sauce-labs-backpack")

    badge = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge"))
    )

    assert badge.text == "1", f"Expected cart badge to be 1"

    inventory_page.open_cart()
    print("Current URL:", browser.current_url)
    WebDriverWait(browser,5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
    )

    cart_items = browser.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) > 0, "No items found in cart"

def test_remove_product_from_cart(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser)
    inventory_page.add_product_to_cart("sauce-labs-backpack")
    inventory_page.open_cart()

    print("Current URL:", browser.current_url)
    cart_item = (By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']")

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(cart_item)
    )

    browser.find_element(By.ID, "remove-sauce-labs-backpack").click()

    WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located(cart_item)
    )

    items = browser.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert len(items) == 0, "Item was not removed from the cart"