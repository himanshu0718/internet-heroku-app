from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By


driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='Forgot Password']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//input[@id='email']").send_keys("himanshucr718lee@gmail.com")
time.sleep(1)

driver.find_element(By.XPATH,"//button[@id='form_submit']").click()
time.sleep(3)


print("Pass")
