from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://demoqa.com/login")
sleep(2)
driver.find_element(By.ID, "newUser").click()
sleep(2)
driver.find_element(By.ID, "firstname").send_keys("Sreehari")
driver.find_element(By.ID, "lastname").send_keys("Test")
driver.find_element(By.ID, "userName").send_keys("sreehari_test")
driver.find_element(By.ID, "password").send_keys("123456Tyui@")
driver.find_element(By.ID, "register").click()


sleep(8)