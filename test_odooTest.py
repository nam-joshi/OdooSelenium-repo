import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Pytest fixture for setting up browser
@pytest.fixture
def driver():
    options = Options()
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    service = Service('/Users/namratajoshi/Downloads/chromedriver-mac-arm64/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

# ✅ Test Case 1: Valid Login
def test_login_valid(driver):
    driver.get("http://localhost:8069")
    assert "Odoo" in driver.title
    time.sleep(2)

    search_bar = driver.find_element(By.NAME, "login")
    search_bar.clear()
    search_bar.send_keys("admin")

    password_bar = driver.find_element(By.NAME, "password")
    password_bar.send_keys("admin")
    password_bar.send_keys(Keys.RETURN)
    login_button= driver.find_element(By.XPATH, "//button[text()='Log in']").click()
    login_button.click()
    time.sleep(3)
    time.sleep(3)
    login_button = driver.find_element(By.CSS_SELECTOR, "button.o-dropdown.dropdown-toggle.dropdown")
    login_button.click()
    time.sleep(5)
    assert "Inbox" in driver.title or "Odoo" in driver.title

# Test Case 2: New Vehicle Creation
def test_new_vehicle_creation(driver):
    driver.get("http://localhost:8069")
    assert "Odoo" in driver.title
    time.sleep(2)
    search_bar = driver.find_element(By.NAME, "login")
    search_bar.clear()
    search_bar.send_keys("admin")
    password_bar = driver.find_element(By.NAME, "password")
    password_bar.send_keys("admin")
    password_bar.send_keys(Keys.RETURN)
    time.sleep(3)
    login_button = driver.find_element(By.CSS_SELECTOR, "button.o-dropdown.dropdown-toggle.dropdown")
    login_button.click()
    time.sleep(10)
    home_menu_button = driver.find_element(By.CSS_SELECTOR, "button.o-dropdown")
    home_menu_button.click()
    time.sleep(2)
    home_menu_button.click()
    home_menu_button.send_keys(Keys.DOWN)  # First down arrow
    time.sleep(1)
    home_menu_button.send_keys(Keys.DOWN)  # Second down arrow
    time.sleep(1)
    home_menu_button.send_keys(Keys.ENTER) 
    time.sleep(5)
    new_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.o-kanban-button-new")
    new_button.click()
    time.sleep(5)
    model_input = driver.find_element(By.ID, "model_id_0")
    model_input.clear()
    model_input.send_keys(Keys.DOWN)
    time.sleep(1)
    model_input.send_keys(Keys.ENTER)
    time.sleep(3)
    driver_input = driver.find_element(By.ID, "driver_id_0")
    driver_input.send_keys("Azure Interior")
    driver_input.send_keys(Keys.ARROW_DOWN)
    driver_input.send_keys(Keys.ENTER)
    time.sleep(3)
    fleet_button = driver.find_element(By.CSS_SELECTOR, "a.o-dropdown-item.o_menu_brand")
    fleet_button.click()
    time.sleep(3)