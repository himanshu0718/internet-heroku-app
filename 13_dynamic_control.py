import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


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






