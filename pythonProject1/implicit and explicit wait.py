from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  # package for time
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome("D:\SELENIUM\chromedriver_win32\chromedriver.exe")
driver.get('https://www.google.com/')

search = driver.find_element(By.ID, "APjFqb")
search.send_keys("selenium")
search.submit()
my_wait = WebDriverWait(driver, 20)  # explicit wait decleariton
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
sl = my_wait.until(ec.presence_of_element_located(By.XPATH, "//h3[text()='Selenium']"))
