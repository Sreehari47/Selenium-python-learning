from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/date-picker")
date_input = driver.find_element(By.ID, "datePickerMonthYearInput")

date_input.click()
date_input.send_keys(Keys.COMMAND + "a")
date_input.send_keys(Keys.DELETE)
date_input.send_keys("07/20/2026")
print(date_input.get_attribute("value"))
date_input.send_keys(Keys.ESCAPE)
driver.save_screenshot("date.png")
input("Press enter to close the browser!")