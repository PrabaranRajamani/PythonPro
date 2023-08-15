from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("D:\SELENIUM\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_96612yg6jw_e&adgrpid=60571832564&hvpone=&hvptwo=&hvadid=610644605478&hvpos=&hvnetw=g&hvrand=14147291052028886926&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9040218&hvtargid=kwd-296458795081&hydadcr=14452_2316413")
driver.maximize_window()
element = driver.find_element(By.XPATH, "//*[@id='twotabsearchtextbox']")
element.send_keys("titan watch for IT Professions")
element.submit()

print("test case done")

driver.close()