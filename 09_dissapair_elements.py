from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='Disappearing Elements']").click()
gallery_count = 0  
no_gallery = 0
n = 5
for i in range(n):
    try:
        if driver.find_element(By.XPATH,"//a[normalize-space()='Gallery']"):
            gallery_count+=1
    except:
        no_gallery +=1
    driver.refresh()
    time.sleep(1)

#we are able to print the number of times gallery element is present after refreshing the webpage n number of times.

print(f"Out of {n} times Gallery was present {gallery_count} times")
print(f"Out of {n} times Dissapaired {no_gallery} times")
