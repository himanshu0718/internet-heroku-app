import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='Dynamic Loading']").click()
time.sleep(1)

# Element 1
driver.find_element(By.XPATH,"//a[normalize-space()='Example 1: Element on page that is hidden']").click()
time.sleep(1)

# Start
driver.find_element(By.XPATH,"//button[normalize-space()='Start']").click()
time.sleep(8)
start_text = driver.find_element(By.XPATH,"//h4[normalize-space()='Hello World!']").text
if start_text == "Hello World!":
    print("element 1 passed")
else:
    print("element 1 func failed")

driver.back()

# Element 2
driver.find_element(By.XPATH,"//a[normalize-space()='Example 2: Element rendered after the fact']").click()
time.sleep(1)

#Start 2
driver.find_element(By.XPATH,"//button[normalize-space()='Start']").click()
time.sleep(8)
start_text_2 = driver.find_element(By.XPATH,"//h4[normalize-space()='Hello World!']").text
if start_text_2 == "Hello World!":
    print("element 2 passed")
else:
    print("element 2 func failed")




