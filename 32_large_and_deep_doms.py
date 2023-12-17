from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='Large & Deep DOM']").click()
time.sleep(1)
action = ActionChains(driver)

#getting Siblings text
sib_text = driver.find_element(By.XPATH,"//div[@id='sibling-50.3']").text
print("Sibling text :- ", sib_text)

#getting table text
table_text = driver.find_element(By.XPATH,"//td[normalize-space()='48.26']")
action.scroll_to_element
print("table text :- ", table_text)