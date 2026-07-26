from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_checkout_empty_fields(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    driver.execute_script("arguments[0].click();", cart_icon)
    time.sleep(5)
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
    )
    checkout_btn = driver.find_element(By.ID, "checkout")
    driver.execute_script("arguments[0].click();", checkout_btn)
    time.sleep(3)
    WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )
    driver.find_element(By.ID, "continue").click()
    error_msg = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )
    assert "First Name is required" in error_msg.text
    print("✅ test_checkout_empty_fields пройден")