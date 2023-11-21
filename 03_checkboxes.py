import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
from selenium.webdriver.common.by import By

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='Checkboxes']").click()
time.sleep(1)

check_box_1 = driver.find_element(By.XPATH,"//input[1]").click()
time.sleep(1)

uncheck_box_2 = driver.find_element(By.XPATH,"//input[2]").click()
time.sleep(1)

uncheck_box_1 = driver.find_element(By.XPATH,"//input[1]").click()
time.sleep(4)

print("Check - uncheck successful")