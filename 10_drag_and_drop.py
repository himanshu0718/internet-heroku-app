from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='Drag and Drop']").click()
time.sleep(1)

source_element = driver.find_element(By.XPATH,"//div[@id='column-a']")
destination = driver.find_element(By.XPATH,"//div[@id='column-b']")

action = ActionChains(driver)
action.click_and_hold(source_element).move_to_element(destination).release(destination).perform()
time.sleep(3)
print("Pass")

