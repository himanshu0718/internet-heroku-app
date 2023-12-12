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


driver.find_element(By.XPATH,"//a[normalize-space()='Frames']").click()
time.sleep(1)

# ---------------------------------
#Nested Frames

driver.find_element(By.XPATH,"//a[normalize-space()='Nested Frames']").click()
time.sleep(1)
print("Nested Frames:- \n")

# left_frame 
driver.switch_to.frame("frame-top")
driver.switch_to.frame(0)
left_text = driver.find_element(By.XPATH,"//body").text
print("The Text in the left frame is", left_text)

#middle frame
driver.switch_to.parent_frame()
driver.switch_to.frame("frame-middle")
middle_text = driver.find_element(By.XPATH,"//div[@id='content']").text
print("The Text in the middle frame is", middle_text)

#right frame
driver.switch_to.parent_frame()
driver.switch_to.frame("frame-right")
right_text = driver.find_element(By.XPATH,"//body").text
print("The Text in the right frame is", right_text)

#bottom frame
driver.switch_to.default_content()
driver.switch_to.frame("frame-bottom")
bottom_text = driver.find_element(By.XPATH,"//body").text
print("The Text in the bottom frame is", bottom_text)
print("Nested Frame Passed.......")

# ----------------------------------------------------------------------------

#iframe

driver.back()

driver.find_element(By.XPATH,"//a[normalize-space()='iFrame']").click()
time.sleep(1)

#selecting iFrame Element
input_field = driver.find_element(By.XPATH,"//iframe[@id='mce_0_ifr']")
driver.switch_to.frame(input_field.click())
time.sleep(1)

#clearing input field
input_field.send_keys(Keys.CONTROL, 'a')
input_field.send_keys(Keys.BACKSPACE)
time.sleep(1)
input_field.send_keys("This is herokuapp automation using python selenium")
time.sleep(2)

print("iFrame Passed........")




