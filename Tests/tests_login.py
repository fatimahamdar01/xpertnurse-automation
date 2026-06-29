from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(driver, email, password):
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_field.clear()
    email_field.send_keys(email)

    password_field = driver.find_element(By.ID, "password")
    password_field.clear()
    password_field.send_keys(password)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()


# Valid Login Test Case
def test_login_valid_credentials(driver):
    login(driver, "fatima@gmail.com", "12345678")

    dashboard = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='nova']/div/div[1]/ul/li[5]/a")
        )
    )

    assert dashboard.is_displayed()

# Invalid Login Test Cases- Invalid Email Format
def test_login_invalid_email_format(driver):
    login(driver, "invalidemail", "12345678")

    email_field = driver.find_element(By.ID, "email")

    assert email_field.get_attribute("validationMessage") != ""


# Invalid Login Test Cases- Invalid Password
def test_login_invalid_password(driver):
    login(driver, "fatima@gmail.com", "wrongpassword")

    error = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p.text-danger"))
    )

    assert error.is_displayed()

