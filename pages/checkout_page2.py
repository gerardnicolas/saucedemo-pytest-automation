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
            EC.element_to_be_clickable(self.finish_btn)
        )
        finish_button.click()

    def cancel_form(self):
        self.driver.find_element(*self.cancel_btn).click()

    def _verify_url(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.url_to_be("checkout-step-two.html")
            )
        except:
            f"Did not reach /checkout-step-two.html page."