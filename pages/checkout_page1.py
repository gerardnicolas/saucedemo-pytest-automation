from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPageOne:
    error_locator = (By.CSS_SELECTOR, "div.error-message-container h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.continue_btn = (By.ID, "continue")
        self.firstname_input = (By.ID, "first-name")
        self.lastname_input = (By.ID, "last-name")
        self.postalcode_input = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")

    def is_displayed(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except:
            return False

    def _snippet_around_error(self, radius=200):
        src = self.driver.page_source or ""
        idx = src.find("Error: Postal Code is required")
        if idx == -1:
            return src[:radius]
        start = max(0, idx - radius)
        end = min(len(src), idx + radius)
        return src[start:end]

