from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://saucedemo.com/")

driver.find_element(By.XPATH,"//input[@name='user-name']").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@type='submit']").click()

driver.find_element(By.ID,'react-burger-menu-btn').click()
time.sleep(1)
driver.find_element(By.ID,'logout_sidebar_link').click()

time.sleep(5)


