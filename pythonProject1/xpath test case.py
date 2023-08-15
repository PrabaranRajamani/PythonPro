from selenium import webdriver
driver = webdriver.Chrome("D:\SELENIUM\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.com")
driver.maximize_window()
actualTitle = driver.title
expectedTitle = "Google"
if actualTitle == expectedTitle:
    print("Verification Successful – Correct title is displayed on the home webpage")
else:
    print("Verification Failed: Incorrect title is displayed on the home webpage")



webElement(driver.find_element_by_id("APjFqb")
driver.close()
