from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By
from PIL import Image


driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)


driver.find_element(By.XPATH,"//a[normalize-space()='Geolocation']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//button[normalize-space()='Where am I?']").click()
time.sleep(3)

lat_value = driver.find_element(By.XPATH,"//div[@id='lat-value']").text
print("Your Latitude value : ", lat_value)

long_value = driver.find_element(By.XPATH,"//div[@id='long-value']").text
print("Your Longitude value : ", long_value)

driver.find_element(By.XPATH,"//a[normalize-space()='See it on Google']").click()
time.sleep(5)

# driver.save_screenshot("D:/coding practise/Projects/The internet - herokuapp/screenshots/location.png")
driver.save_screenshot("your_location.png")
image = Image.open("your_location.png")
image.show()
driver.close()

print("pass")




