from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.XPATH,"//a[normalize-space()='Basic Auth']").click()
time.sleep(1)
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(1)
driver.find_element(By.XPATH,"//p[contains(text(),'Congratulations! You must have the proper credenti')]")
print("AUTHENTICATION SUCCESSFUL")