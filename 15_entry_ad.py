from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By


driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='Entry Ad']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//p[normalize-space()='Close']").click()
time.sleep(1)

#clicking click here 2 times to produce popup again
driver.find_element(By.ID,"restart-ad").click()
time.sleep(1)
driver.find_element(By.ID,"restart-ad").click()
time.sleep(3)

driver.find_element(By.XPATH,"//p[normalize-space()='Close']").click()
print("pass")




