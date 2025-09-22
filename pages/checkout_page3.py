from selenium.webdriver.common.by import By

class CheckoutPageThree:
    go_back_to_products_btn = (By.ID, "back-to-products")
    thank_you_msg = (By.LINK_TEXT, "Thank you for your order!")
    success_header_message = (By.CSS_SELECTOR, ".complete-header")

    def __init__(self, driver):
        self.driver = driver

    def go_back_to_products(self):
        self.driver.find_element(*self.go_back_to_products_btn).click()

    def _get_success_message(self):
        return self.driver.find_element(*self.success_header_message).text