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

# Test Case 1: Valid Login
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

# Test Case 3: Required Field in Contract
def test_new_contract_required_field(driver):
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
    fleet_button = driver.find_element(By.XPATH, "//button[@data-menu-xmlid='fleet.fleet_vehicles']")
    fleet_button.click()
    time.sleep(2)
    contracts_link = driver.find_element(By.XPATH, "//a[@data-menu-xmlid='fleet.fleet_vehicle_log_contract_menu']")
    contracts_link.click()
    time.sleep(2)
    new_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.o_list_button_add")
    new_button.click()
    time.sleep(3)
    name_field = driver.find_element(By.ID, "name_0")
    name_field.send_keys("Contract Name")
    time.sleep(3)
    fleet_button = driver.find_element(By.CSS_SELECTOR, "a.o-dropdown-item.o_menu_brand")
    fleet_button.click()
    time.sleep(3)
    vehicle_label = driver.find_element(By.CSS_SELECTOR, "label.o_form_label[for='vehicle_id_0']")
    # Get its color
    label_color = vehicle_label.value_of_css_property("color")
    # Print or assert
    print("Label color:", label_color)
    assert "rgba(210, 63, 58, 1)" in label_color, "Vehicle label is not showing error in red"

# Test Case 4: New Contract Creation
def test_new_contract_creation(driver):
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
    fleet_button = driver.find_element(By.XPATH, "//button[@data-menu-xmlid='fleet.fleet_vehicles']")
    fleet_button.click()
    time.sleep(2)
    contracts_link = driver.find_element(By.XPATH, "//a[@data-menu-xmlid='fleet.fleet_vehicle_log_contract_menu']")
    contracts_link.click()
    time.sleep(2)
    new_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.o_list_button_add")
    new_button.click()
    time.sleep(3)
    name_field = driver.find_element(By.ID, "name_0")
    name_field.send_keys("Contract Name")
    time.sleep(3)
    vehicle_dropdown = driver.find_element(By.ID, "vehicle_id_0")
    vehicle_dropdown.click()
    vehicle_dropdown.send_keys(Keys.DOWN)
    time.sleep(1)
    vehicle_dropdown.send_keys(Keys.ENTER)
    time.sleep(2)
    fleet_button = driver.find_element(By.CSS_SELECTOR, "a.o-dropdown-item.o_menu_brand")
    fleet_button.click()
    time.sleep(3)

# Test Case 5: Unique Category
def test_new_contract_creation(driver):
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
    config_button = driver.find_element(By.XPATH, "//button[@data-menu-xmlid='fleet.fleet_configuration']")
    config_button.click()
    time.sleep(3)
    categories_link = driver.find_element(By.XPATH, "//a[@data-menu-xmlid='fleet.fleet_vehicle_model_category_menu' and text()='Categories']")
    categories_link.click()
    time.sleep(2)
    new_button1 = driver.find_element(By.XPATH, "//button[contains(@class, 'o_list_button_add') and text()=' New ']")
    new_button1.click()
    time.sleep(2)
    name_input = driver.find_element(By.XPATH, "//div[@name='name']//input[@class='o_input']")
    name_input.send_keys("Sedan")
    name_input.send_keys(Keys.ENTER)
    time.sleep(2)
    error_modal = driver.find_element(By.XPATH, "//h4[text()='Validation Error']")
    assert error_modal.is_displayed()
