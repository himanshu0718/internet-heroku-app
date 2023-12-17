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

driver.find_element(By.XPATH,"//a[normalize-space()='WYSIWYG Editor']").click()
time.sleep(1)

#selecting iframe element
input_field = driver.find_element(By.XPATH,"//iframe[@id='mce_0_ifr']")
driver.switch_to.frame(input_field.click())
time.sleep(1)

#clearing input field
input_field.send_keys(Keys.CONTROL, 'a')
input_field.send_keys(Keys.BACKSPACE)
time.sleep(1)
input_field.send_keys("This is herokuapp automation using python selenium")
time.sleep(3)

print("Passed")
