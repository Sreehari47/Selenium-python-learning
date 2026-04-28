from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#driver.find_element(By.XPATH,"//input[@name='user-name']").send_keys("standard_user")
#driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("secret_sauce")
#driver.find_element(By.XPATH,"//input[@type='submit']").click()

time.sleep(5)
driver.find_element(By.CSS_SELECTOR,".orangehrm-login-forgot").click()
time.sleep(5)


