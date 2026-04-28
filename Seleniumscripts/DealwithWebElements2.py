from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://saucedemo.com/")
#username = driver.find_element(By.NAME,"user-name")
#print(type(username))

#username.send_keys("standard_user")
#password = driver.find_element(By.ID,"password")
#password.send_keys("secret_sauce")
#login_button = driver.find_element(By.CLASS_NAME,"submit-button")
#login_button.click()

driver.find_element(By.XPATH,"//input[@name='user-name']").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@type='submit']").click()


time.sleep(5)


