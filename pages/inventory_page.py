from selenium.webdriver.common.by import By

class InventoryPage():
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    cart_badge = (By.CSS_SELECTOR, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self, product_id):
        add_btn = (By.ID, f"add-to-cart-{product_id}")
        self.driver.find_element(*add_btn).click()

    def remove_product_from_cart(self, product_id):
        remove_btn = (By.ID, f"remove-{product_id}")
        self.driver.find_element(*remove_btn).click()

    def get_cart_count(self):
        try:
            return int(self.driver.find_element(*self.cart_badge).text)
        except:
            return 0

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def check_item_detail(self, product_id):
        img_btn = (By.CSS_SELECTOR, f"img[alt='{product_id}']")
        self.driver.find_element(*img_btn).click()
