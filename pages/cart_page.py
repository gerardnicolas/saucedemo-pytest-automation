from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from conftest import browser


class CartPage:
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    cart_quantity = (By.CSS_SELECTOR, ".cart_quantity")
    item_names = (By.CLASS_NAME, "inventory_item_name")


    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def _has_item(self, item_name: str) -> bool:
        items = self.driver.find_elements(*self.item_names)
        return any(item.text == item_name for item in items)

    def _verify_item_in_cart(self):
        cart_items = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "cart_item"))
        )

        return len(cart_items) > 0, "No items found in cart"

    def _assert_cart_is_empty(self):
        try:
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
            )
        except TimeoutException:
            raise AssertionError("Cart is not empty!")

    def _remove_item(self, item):
        remove_btn = (By.ID, f"remove-{item}")
        self.driver.find_element(*remove_btn).click()

    def _is_empty(self):
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return len(items) == 0, f"Cart must be empty. Cart has {items} remaining."

    def _go_back_to_inventory(self):
        continue_shopping_btn = (By.ID, "continue-shopping")
        self.driver.find_element(*continue_shopping_btn).click()

    def _click_checkout(self):
        checkout_btn = (By.ID, "checkout")
        self.driver.find_element(*checkout_btn).click()

        # Wait for next page
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "checkout_info_container"))
        )