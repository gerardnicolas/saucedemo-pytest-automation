import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()

    # Disable Chrome's password manager + leak detection popups
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }
    options.add_experimental_option("prefs", prefs)

    # Run in incognito for clean sessions
    options.add_argument("--incognito")

    # Initialize Chrome via webdriver-manager
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
