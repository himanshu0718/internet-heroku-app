import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='Dropdown']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//select[@id='dropdown']").click()
time.sleep(1)

Select(driver.find_element(By.XPATH,"//select[@id='dropdown']")).select_by_value("1")
time.sleep(1)

driver.find_element(By.XPATH,"//select[@id='dropdown']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//select[@id='dropdown']").click()
time.sleep(1)   

Select(driver.find_element(By.XPATH,"//select[@id='dropdown']")).select_by_value("2")
time.sleep(1)

driver.find_element(By.XPATH,"//select[@id='dropdown']").click()
time.sleep(1)

print("Pass")



