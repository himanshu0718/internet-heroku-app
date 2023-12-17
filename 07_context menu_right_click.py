from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[normalize-space()='Context Menu']").click()
time.sleep(1)

rightclick = ActionChains(driver)
box = driver.find_element(By.XPATH,"//div[@id='hot-spot']")
rightclick.context_click(box).perform()
time.sleep(2)

alert_obj = driver.switch_to.alert
alert_obj.accept()
time.sleep(2)

