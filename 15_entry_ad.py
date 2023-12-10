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

driver.find_element(By.XPATH,"//a[normalize-space()='Entry Ad']").click()
time.sleep(1)

driver.find_element(By.XPATH,"//p[normalize-space()='Close']").click()
time.sleep(1)

#clicking click here 2 times to produce popup again
driver.find_element(By.ID,"restart-ad").click()
time.sleep(1)
driver.find_element(By.ID,"restart-ad").click()
time.sleep(3)

driver.find_element(By.XPATH,"//p[normalize-space()='Close']").click()
print("pass")




