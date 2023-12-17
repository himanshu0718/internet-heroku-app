from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By


driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='Typos']").click()
time.sleep(1)


typo_text = "Sometimes you'll see a typo, other times you won,t."
c = 0

for i in range(5):
    TEXT = driver.find_element(By.XPATH,"//p[2]").text 
    if TEXT == typo_text:
        # print("typo is present")
        c += 1
    else:
        pass
        # print("no typo present")
    driver.refresh()

print(f"Out of 5 times Typo error was present : {c} times")

