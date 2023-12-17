from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By
from pyshadow.main import Shadow

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.XPATH,"//a[normalize-space()='Shadow DOM']").click()
time.sleep(1)
shadow = Shadow(driver)

First_block_Text = shadow.find_element("span[slot='my-text']").text
print("First block :-\n",First_block_Text)

Second_block_text= shadow.find_element("ul[slot='my-text']").text
print("Second block :-\n",Second_block_text)

