import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = "https://xpertnurse.xpertbotacademy.online/admin/login"


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(LOGIN_URL)
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_field.clear()
    email_field.send_keys("fatima@gmail.com")

    password_field = driver.find_element(By.ID, "password")
    password_field.clear()
    password_field.send_keys("12345678")

    # Wait for submit button to be clickable before clicking
    submit_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    submit_btn.click()

    # Wait until dashboard is fully loaded
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='nova']/div/div[1]/ul/li[5]/a")
        )
    )

    return driver