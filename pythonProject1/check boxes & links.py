
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("D:\SELENIUM\chromedriver_win32\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# for choose one box

# choose = driver.find_element(By.XPATH , "//input[contains(@id,'monday')]")
# choose.click()

# for choose all boxes

checkboxes = driver.find_elements(By.XPATH, "//input[contains(@id, 'day')]")


for checkbox in checkboxes:
    checkbox.click()