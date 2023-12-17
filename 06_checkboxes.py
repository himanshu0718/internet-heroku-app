from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='Checkboxes']").click()
time.sleep(1)

check_box_1 = driver.find_element(By.XPATH,"//input[1]").click()
time.sleep(1)

uncheck_box_2 = driver.find_element(By.XPATH,"//input[2]").click()
time.sleep(1)

uncheck_box_1 = driver.find_element(By.XPATH,"//input[1]").click()
time.sleep(4)

print("Check - uncheck successful")