import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in browser.current_url

def test_invalid_login(browser):
    login_page = LoginPage(browser)
    login_page.login("wrong_user", "secret_sauce")
    error_message = browser.find_element(*LoginPage.error_message)
    assert error_message.is_displayed()

def test_locked_out_user_login(browser):
    login_page = LoginPage(browser)
    login_page.login("locked_out_user", "secret_sauce")
    error_message = login_page.receive_error()
    assert "Epic sadface" in error_message

def test_problem_user_login(browser):
    login_page = LoginPage(browser)
    login_page.login("problem_user", "secret_sauce")
    WebDriverWait(browser, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )

    items = browser.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) == 6, f"Expected 6 items, found {len(items)}"

def test_performance_glitch_user_login(browser):
    login_page = LoginPage(browser)
    login_page.login("performance_glitch_user", "secret_sauce")

    items = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
    )

    assert len(items) == 6, f"Expected 6 items, found {len(items)}"
