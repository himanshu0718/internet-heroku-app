from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By


driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='Dropdown']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//select[@id='dropdown']").click()
time.sleep(1)

Select(driver.find_element(By.XPATH,"//select[@id='dropdown']")).select_by_value("1")
time.sleep(1)

driver.find_element(By.XPATH,"//select[@id='dropdown']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//select[@id='dropdown']").click()
time.sleep(1)   

Select(driver.find_element(By.XPATH,"//select[@id='dropdown']")).select_by_value("2")
time.sleep(1)

driver.find_element(By.XPATH,"//select[@id='dropdown']").click()
time.sleep(1)

print("Pass")



