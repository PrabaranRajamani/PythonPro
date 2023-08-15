from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://selenium08.blogspot.com/2019/08/radio-buttons.html")
driver.find_element(By.NAME,"red").click()
