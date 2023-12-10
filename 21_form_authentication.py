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


driver.find_element(By.XPATH,"//a[normalize-space()='Form Authentication']").click()
time.sleep(1)

#enter username and passward for correct login
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("tomsmith")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("SuperSecretPassword!")
time.sleep(1)
driver.find_element(By.XPATH,"//i[@class='fa fa-2x fa-sign-in']").click()

time.sleep(1)
secure_TEXT = driver.find_element(By.XPATH,"//h2[normalize-space()='Secure Area']").text
if secure_TEXT == "Secure Area":
    print("login success")
else:
    print("Incorrect login")

time.sleep(1)
driver.find_element(By.XPATH,"//i[@class='icon-2x icon-signout']").click()
time.sleep(1)

#enter username and passward for incorrect login

driver.find_element(By.XPATH,"//input[@id='username']").send_keys("username")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Passward")
time.sleep(1)
driver.find_element(By.XPATH,"//i[@class='fa fa-2x fa-sign-in']").click()
time.sleep(1)
incorrect_TEXT = driver.find_element(By.XPATH,"//div[@id='flash']").text

if incorrect_TEXT: 
    print("INcorrect login success")
else:
    print("error")

print("Authentication Complete")







