from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import browser


class CheckoutPageOne:
    firstname_input = (By.ID, "first-name")
    lastname_input = (By.ID, "last-name")
    postalcode_input = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver

    def fill_up_form(self, firstname, lastname, postalcode):
        self.driver.find_element(*self.lastname_input).send_keys(lastname)
        self.driver.find_element(*self.postalcode_input).send_keys(postalcode)

    def continue_form(self):
        self.driver.find_element(*self.continue_btn).click()

