from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome( "D:\SELENIUM\chromedriver_win32\chromedriver.exe" )
driver.get('https://demo.nopcommerce.com/')
# element = driver.find_element_by_link_text('Log in')
# element.click()
elements = elements = driver.find_elements(By.XPATH, "//*[@id='small-searchterms']")

print(len(elements))
