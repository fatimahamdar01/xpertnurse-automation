from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_user(logged_in_driver):
    driver = logged_in_driver

    driver.get("https://xpertnurse.xpertbotacademy.online/admin/resources/users")

    # Wait for "Create User" button and click
    create_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='nova']/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/a")
        )
    )
    create_btn.click()

    # Fill in the form
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "name"))
    ).send_keys("John Doe")

    driver.find_element(By.ID, "email").send_keys("johndoe@gmail.com")
    driver.find_element(By.ID, "password").send_keys("12345678")

    # Wait for save button and click
    save_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[@id='nova']/div/div[2]/div[2]/div[2]/form/div[2]/button[2]/span")
        )
    )
    save_btn.click()

    # Assert user was created successfully
    success = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success, [class*='success']"))
    )
    assert success.is_displayed()