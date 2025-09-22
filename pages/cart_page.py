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

    def _go_back_to_inventory(self):
        continue_shopping_btn = (By.ID, "continue-shopping")
        self.driver.find_element(*continue_shopping_btn).click()

    def _click_checkout(self, timeout: int = 20):
        self.driver.find_element(*self.checkout_btn).click()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-one.html")
        )