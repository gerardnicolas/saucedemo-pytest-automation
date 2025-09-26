from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPageThree:
    go_back_to_products_btn = (By.ID, "back-to-products")
    thank_you_msg = (By.LINK_TEXT, "Thank you for your order!")
    success_header_message = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def go_back_to_products(self):
        self.driver.find_element(*self.go_back_to_products_btn).click()

    def _get_success_message(self):
        return self.driver.find_element(*self.success_header_message).text

    def _is_displayed(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element.is_displayed()
        except:
            return False