# SauceDemo Test Automation (Pytest + Selenium)

Automated test suite for [saucedemo.com](https://www.saucedemo.com), built using **Python, Pytest, and Selenium WebDriver**.  
This project follows the **Page Object Model (POM)** design pattern for maintainability, scalability, and readability.  

Demonstrates an approach **end-to-end functional UI testing** with a real-world e-commerce sample application.

---

## 🔹 Key Highlights
- ✅ **Page Object Model (POM):** clean separation between test logic and UI locators/actions.  
- ✅ **Pytest Fixtures:** reusable setup/teardown with flexible browser management.  
- ✅ **Explicit Waits (WebDriverWait):** reliable synchronization for dynamic elements.  
- ✅ **HTML Reports:** easy-to-share test execution reports (`pytest-html`).  
- ✅ **Scalable Structure:** can be extended to cover larger test suites and CI/CD pipelines.  

**Skills Demonstrated:**  
`Python` · `Selenium WebDriver` · `Pytest` · `Automation Framework Design` · `Page Object Model (POM)` · `Test Reporting` · `Continuous Integration Ready`

---

## 🔹 Project Structure

```text
saucedemo-pytest-automation/
│
├── pages/                  # Page Object classes
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page1.py
│   ├── checkout_page2.py
│   └── checkout_page3.py
│
├── tests/                  # Test cases
│   ├── test_login.py
│   ├── test_addtocart.py
│   └── test_checkout_item.py
│
├── conftest.py             # Pytest configuration & browser fixture
├── requirements.txt        # Project dependencies
└── README.md               # Documentation
```
---
## 🔹 Installation and Setup
1. Clone the repository
```bash
git clone https://github.com/gerardnicolas/saucedemo-pytest-automation.git
cd saucedemo-pytest-automation
```
2. Create & activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```
2. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔹 Running Tests
1. Run the full test suite:
```bash
pytest -v
```
2. Run a specific test file:
```bash
pytest -v tests/test_login.py
```
2. Run with HTML report:
```bash
pytest -v --html=report.html
```

---

## Example Test Flow
Test Case: Successful login
- Open saucedemo.com login page
- Enter valid credetials
- Click login
- Assert that the user is redirected to the inventory page
```python
def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in browser.current_url
```

---

## Why This Matters
This framework is designed with long-term software quality in mind:

- **Scalable** — structured so new test cases and modules can be added with minimal effort.  
- **Maintainable** — Page Object Model (POM) ensures a clean separation between test logic and UI locators/actions.  
- **Reliable** — explicit waits and fixtures reduce flaky tests and improve consistency across runs.  
- **CI/CD Ready** — organized for seamless integration with pipelines and automated reporting.  

