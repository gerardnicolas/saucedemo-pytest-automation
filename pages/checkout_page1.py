from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPageOne:
    def __init__(self, driver):
        self.driver = driver
        self.continue_btn = (By.ID, "continue")
        self.firstname_input = (By.ID, "first-name")
        self.lastname_input = (By.ID, "last-name")
        self.postalcode_input = (By.ID, "postal-code")

    def fill_input_field(self, locator, value, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.clear()
        element.send_keys(str(value))
        return element

    def _click_continue(self):
        self.driver.find_element(*self.continue_btn).click()

    def _verify_url(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.url_to_be("checkout-step-one.html")
            )
        except:
            f"Did not reach /checkout-step-one.html page."