from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://google.com")
myPageTitle=driver.title
print(myPageTitle)
assert "Google" in myPageTitle
print(driver.quit())
#driver.quit()