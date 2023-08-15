from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("D:\SELENIUM\chromedriver_win32\chromedriver.exe")
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

# self
text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'Kalyan Jewellers Ind')]/self::a").text
print(text_msg) # Kalyan Jewellers Ind


# parent
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'Kalyan Jewellers Ind')]/parent::td").text
# print(text_msg)

# child
# child = driver.find_elements(By.XPATH, "//a[contains(text(),'Kalyan Jewellers Ind')]/ancestor::tr/child::td")
# print(len(child))  # 5

# ancestor
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'Kalyan Jewellers Ind')]/ancestor::tr").text
# print(text_msg)  # Kalyan Jewellers Ind A 142.05 147.00 + 3.48

# following
# following = driver.find_elements(By.XPATH,"//a[contains(text(),'Kalyan Jewellers Ind')]/ancestor::tr/following::*")
# print(len(following))  # 3162
