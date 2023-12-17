from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)


driver.find_element(By.XPATH,"//a[normalize-space()='Horizontal Slider']").click()
time.sleep(1)

#slider move by click and hold
slider = driver.find_element(By.XPATH,"//input[@value='0']")
move = (ActionChains(driver))
move.click_and_hold(slider).move_by_offset(40,0).release().perform()
move.click_and_hold(slider).move_by_offset(-20,0).release().perform()
time.sleep(3)

# slider by arrow keys
focus = slider.click()
move.send_keys(Keys.ARROW_RIGHT).perform()
time.sleep(0.3)
move.send_keys(Keys.ARROW_RIGHT).perform()
time.sleep(0.3)
move.send_keys(Keys.ARROW_RIGHT).perform()
time.sleep(0.3)
move.send_keys(Keys.ARROW_RIGHT).perform()
time.sleep(0.3)
move.send_keys(Keys.ARROW_LEFT).perform()
time.sleep(0.3)
move.send_keys(Keys.ARROW_LEFT).perform()
time.sleep(0.3)
move.send_keys(Keys.ARROW_LEFT).perform()
time.sleep(0.3)
move.send_keys(Keys.ARROW_LEFT).perform()
time.sleep(0.3)


print("pass")



