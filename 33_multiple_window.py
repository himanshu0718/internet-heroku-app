from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='Multiple Windows']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='Click Here']").click()
time.sleep(1)

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    time.sleep(2)
    print(driver.title)




