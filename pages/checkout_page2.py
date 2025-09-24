from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CheckoutPageTwo:
    def __init__(self, driver):
        self.driver = driver
        self.finish_btn = (By.ID, "finish")
        self.cancel_btn = (By.ID, "cancel")

    def _click_finish(self, timeout=20):
        finish_button = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.finish_btn)
        )
        finish_button.click()

    def cancel_form(self):
        self.driver.find_element(*self.cancel_btn).click()

    def _verify_url(self):
        WebDriverWait(self.driver, 20).until(
            EC.url_to_be("https://www.saucedemo.com/checkout-step-two.html")
        )