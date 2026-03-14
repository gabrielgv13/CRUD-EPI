from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_login_success(driver, base_url, login_email, login_password, existing_login_user):
	wait = WebDriverWait(driver, 10)

	driver.get(base_url)
	assert "Login" in driver.title

	email_input = wait.until(EC.element_to_be_clickable((By.ID, "email")))
	email_input.clear()
	email_input.send_keys(login_email)

	password_input = wait.until(EC.element_to_be_clickable((By.ID, "password")))
	password_input.clear()
	password_input.send_keys(login_password)

	submit_button = wait.until(
		EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'].submit-btn"))
	)
	submit_button.click()

	wait.until(EC.url_contains("/dashboard"))
	assert "Estoque de EPI" in driver.title

def test_create_login_success(driver, base_url, new_login_credentials):
    wait = WebDriverWait(driver, 10)

    driver.get(base_url)
    assert "Login" in driver.title

    submit_button = wait.until(
		EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/login_create']"))
	)
    submit_button.click()

    email_input = wait.until(EC.element_to_be_clickable((By.ID, "email")))
    email_input.clear()
    email_input.send_keys(new_login_credentials["email"])

    password_input = wait.until(EC.element_to_be_clickable((By.ID, "password")))
    password_input.clear()
    password_input.send_keys(new_login_credentials["password"])

    password_input = wait.until(EC.element_to_be_clickable((By.ID, "cf_password")))
    password_input.clear()
    password_input.send_keys(new_login_credentials["password"])

    submit_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'].submit-btn"))
    )
    submit_button.click()

    wait.until(EC.url_contains("/dashboard"))
    assert "Estoque de EPI" in driver.title