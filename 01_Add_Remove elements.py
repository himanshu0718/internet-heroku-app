import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.XPATH,"//a[normalize-space()='Add/Remove Elements']").click()
time.sleep(2)


#adding 2 elements
driver.find_element(By.XPATH,"//button[normalize-space()='Add Element']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//button[normalize-space()='Add Element']").click()
time.sleep(1)

#deleting 2 added elements
driver.find_element(By.XPATH,"//body[1]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
time.sleep(1)
driver.find_element(By.XPATH,"//body[1]/div[2]/div[1]/div[1]/div[1]/button[1]").click()
time.sleep(2)

print("SUCCESSFULLY ADDED AND DELETED ELEMENTS")

#you can also import random module to add random number of elements
#then delete all of them using while loop
