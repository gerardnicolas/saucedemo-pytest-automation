import pytest
from selenium import webdriver
@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")  # modern headless mode
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)  # ✅ No need for webdriver_manager
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()