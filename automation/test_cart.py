from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    driver.find_element(By.XPATH, "//button[text()='Add to cart']").click()
    cart_badge = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert cart_badge.text == "1"
    print("✅ test_add_to_cart пройден")

def test_remove_from_cart(driver):
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
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)
    # Ждём заголовок "Your Cart"
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//span[text()='Your Cart']"))
    )
    # Ждём, что хотя бы один товар есть в корзине
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_item"))
    )
    driver.find_element(By.XPATH, "//button[text()='Remove']").click()
    # Ждём, пока бейдж исчезнет
    WebDriverWait(driver, 20).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    cart_badge_after = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(cart_badge_after) == 0
    print("✅ test_remove_from_cart пройден")