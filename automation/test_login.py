import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- Шаги с декораторами @allure.step ---
@allure.step("Открываем страницу логина")
def open_login_page(driver):
    driver.get("https://www.saucedemo.com/")

@allure.step("Вводим логин: {username}")
def enter_username(driver, username):
    driver.find_element(By.ID, "user-name").send_keys(username)

@allure.step("Вводим пароль: {password}")
def enter_password(driver, password):
    driver.find_element(By.ID, "password").send_keys(password)

@allure.step("Нажимаем кнопку Login")
def click_login_button(driver):
    driver.find_element(By.ID, "login-button").click()

@allure.step("Ждём загрузки страницы товаров")
def wait_for_inventory_page(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

@allure.step("Проверяем URL на наличие /inventory.html")
def assert_inventory_url(driver):
    assert "/inventory.html" in driver.current_url

# --- Тесты ---
def test_login_success(driver):
    open_login_page(driver)
    enter_username(driver, "standard_user")
    enter_password(driver, "secret_sauce")
    click_login_button(driver)
    wait_for_inventory_page(driver)
    assert_inventory_url(driver)
    print("✅ test_login_success пройден")

def test_login_locked_user(driver):
    open_login_page(driver)
    enter_username(driver, "locked_out_user")
    enter_password(driver, "secret_sauce")
    click_login_button(driver)
    error_msg = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )
    assert "locked out" in error_msg.text
    print("✅ test_login_locked_user пройден")

def test_login_wrong_password(driver):
    open_login_page(driver)
    enter_username(driver, "standard_user")
    enter_password(driver, "wrong_password")
    click_login_button(driver)
    error_msg = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )
    assert "Username and password do not match" in error_msg.text
    print("✅ test_login_wrong_password пройден")