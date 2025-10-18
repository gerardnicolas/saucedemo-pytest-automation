from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    """ Wait Methods """
    def wait_for_element_visible(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    """ Interaction Methods """
    def click(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    def type(self, locator, text, clear=True):
        element = self.wait_for_element_visible(locator)
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait_for_element_visible(locator)
        return element.text

    def get_attribute(self, locator, attribute):
        element = self.wait_for_element_visible(locator)
        return element.get_attribute(attribute)

    def clear_text(self, locator):
        element = self.wait_for_element_visible(locator)
        element.clear()

    """ State Checking """
    def is_element_displayed(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    """ Utility Methods """
    def go_to_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def scroll_into_view(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true)", element)

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    def refresh_page(self):
        self.driver.refresh()