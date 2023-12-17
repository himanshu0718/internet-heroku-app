from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By



driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='Notification Messages']").click()
time.sleep(1)

for i in range(5):    
    driver.find_element(By.XPATH,"//a[normalize-space()='Click here']").click()
    # time.sleep(1)
    TEXT = driver.find_element(By.XPATH,"//div[@id='flash']").text
    print(TEXT)
