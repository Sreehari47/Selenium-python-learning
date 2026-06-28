from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com")
driver.find_element(By.XPATH,"//input[@name='user-name']").send_keys("standard_user")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@id='login-button']").click()

#Handle the dropdown
sort_element = driver.find_element(By.CLASS_NAME, "product_sort_container")
sortDD = Select(sort_element)

#Selecting by index
sortDD.select_by_index(0)
#Selecting by value
sortDD.select_by_value("lohi")
#Selecting by visible text
sortDD.select_by_visible_text("Price (low to high)")

sleep(5)
