from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://google.com")

print(driver.title)

assert driver.title == "Google"

driver.quit()