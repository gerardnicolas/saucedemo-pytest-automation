from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class CheckoutPageTwo:
    finish_btn = (By.CSS_SELECTOR, ".btn.btn_action.btn_medium.cart_button")
    cancel_btn = (By.CSS_SELECTOR, ".btn.btn_secondary.back.btn_medium.cart_cancel_link")

    def __init__(self, driver):
        self.driver = driver

    def finish_form(self):
        # WebDriverWait(self.driver, 5).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn_action.btn_medium.cart_button"))
        # )
        self.driver.find_element(*self.finish_btn).click()

    def cancel_form(self):
        self.driver.find_element(*self.cancel_btn).click()