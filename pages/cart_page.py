from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CartPage:
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    cart_quantity = (By.CSS_SELECTOR, ".cart_quantity")
    item_names = (By.CLASS_NAME, "inventory_item_name")
    checkout_btn = (By.ID, "checkout")

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
        btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_btn)
        )
        btn.click()