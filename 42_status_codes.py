from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By

#function for slow and smooth scrolling to the bottom
def pageBottom(driver):
    bottom=False
    a=0
    while not bottom:
        new_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script(f"window.scrollTo(0, {a});")
        if a > new_height:
            bottom=True
        a+=5


driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='Status Codes']").click()
time.sleep(1)

#to view full list of codes
driver.find_element(By.XPATH,"//a[normalize-space()='here']").click()
pageBottom(driver)
time.sleep(2)
driver.back()

#checking is status code
driver.find_element(By.XPATH,"//a[normalize-space()='200']").click()
time.sleep(2)
driver.back()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='301']").click()
time.sleep(2)
driver.back()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='404']").click()
time.sleep(2)
driver.back()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='500']").click()
time.sleep(2)
driver.back()
time.sleep(1)

print("code checking successful")





