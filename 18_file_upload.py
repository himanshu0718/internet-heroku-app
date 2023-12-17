from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='File Upload']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys("C:/Users/himan/OneDrive/Pictures/Screenshots/permission required_assignment.png")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='file-submit']").click()
time.sleep(5)
print("Pass")