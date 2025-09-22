from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPageOne:
    firstname_input = (By.CSS_SELECTOR, "#first-name")
    lastname_input = (By.CSS_SELECTOR, "#last-name")
    postalcode_input = (By.CSS_SELECTOR, "#postal-code")
    continue_btn = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver

    def _fill_input_field(self, locator, value, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        element.clear()
        element.send_keys(str(value))

    def _click_continue(self):
        self.driver.find_element(*self.continue_btn).click()