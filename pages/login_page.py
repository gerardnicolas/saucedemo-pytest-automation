from unittest import expectedFailure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def receive_error(self):
        return self.driver.find_element(*self.error_message).text