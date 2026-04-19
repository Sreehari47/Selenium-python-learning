from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.google.com")

MypageTitle = driver.title
print(MypageTitle)
assert "Google" in MypageTitle
driver.quit()