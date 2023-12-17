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

driver.find_element(By.XPATH,"//a[normalize-space()='Key Presses']").click()
time.sleep(1)

inp_field = driver.find_element(By.XPATH,"//input[@id='target']")
inp_field.send_keys(Keys.ALT)
print(driver.find_element(By.XPATH,"//p[@id='result']").text)
inp_field.send_keys(Keys.ARROW_DOWN)
print(driver.find_element(By.XPATH,"//p[@id='result']").text)
inp_field.send_keys(Keys.BACK_SPACE)
print(driver.find_element(By.XPATH,"//p[@id='result']").text)
inp_field.send_keys(Keys.CONTROL)
print(driver.find_element(By.XPATH,"//p[@id='result']").text)
inp_field.send_keys(Keys.DELETE)
print(driver.find_element(By.XPATH,"//p[@id='result']").text)

print("Actions working correctly..")
