from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

tests_status = [0, 0, 0]

# Test: Acessar a página de login com uma conta já criada e verificar se o login é bem-sucedido
try:
	driver.get("http://127.0.0.1:8000/")
	assert "Login" in driver.title

	email_input = wait.until(EC.element_to_be_clickable((By.ID, "email")))
	email_input.clear()
	email_input.send_keys("gmail@gmail.com")

	password_input = wait.until(EC.element_to_be_clickable((By.ID, "password")))
	password_input.clear()
	password_input.send_keys("gmail")

	submit_button = wait.until(
		EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'].submit-btn"))
	)
	submit_button.click()

	wait.until(EC.url_contains("/dashboard"))
	assert "Estoque de EPI" in driver.title
	tests_status[0] = 1
finally:
	driver.quit()
	
def check_status():
    status = ["FALHOU", "FALHOU", "FALHOU"]
    for i in range(3):
        if tests_status[i] == 1:
            status[i] = "PASSOU"
    print(status)