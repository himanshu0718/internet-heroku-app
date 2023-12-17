from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By


driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='Dynamic Controls']").click()
time.sleep(1)


#Remove button
driver.find_element(By.XPATH,"//button[normalize-space()='Remove']").click()
time.sleep(5)

Remove_text = driver.find_element(By.XPATH,"//p[@id='message']").text

if Remove_text == "It's gone!":
    print("\nRemove functionality is working correctly\n")
else:
    print("Remove functionality has failed\n")


#Add button
driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
time.sleep(5)

Remove_text = driver.find_element(By.XPATH,"//p[@id='message']").text

if Remove_text == "It's back!":
    print("Add functionality is working correctly\n")
else:
    print("Add functionality has failed\n")


#Enable Button
driver.find_element(By.XPATH,"//button[normalize-space()='Enable']").click()
time.sleep(5)

Text2 = driver.find_element(By.XPATH,"//p[@id='message']").text

if Text2 == "It's enabled!":
    print("Enable functionality is working correctly\n")
else:
    print("Enable functionality has failed\n")


#Disable button
driver.find_element(By.XPATH,"//button[normalize-space()='Disable']").click()
time.sleep(5)

Text2 = driver.find_element(By.XPATH,"//p[@id='message']").text

if Text2 == "It's disabled!":
    print("Disable functionality is working correctly\n")
else:
    print("Disable functionality has failed\n")






