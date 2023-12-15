import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)


driver.find_element(By.XPATH,"//a[normalize-space()='Hovers']").click()
time.sleep(1)

#hovering on 1st element
element = driver.find_element(By.XPATH,"//div[@class='example']//div[1]//img[1]")
hover = ActionChains(driver).move_to_element(element)
hover.perform()
time.sleep(1)
#viewing profile
driver.find_element(By.XPATH,"//div[@class='example']//div[1]//div[1]//a[1]").click()
time.sleep(2)
driver.back()
driver.refresh()
time.sleep(1)

element2 = driver.find_element(By.XPATH,"//div[@class='example']//div[2]//img[1]")
hover = ActionChains(driver).move_to_element(element2)
hover.perform()
time.sleep(2)

element3 = driver.find_element(By.XPATH,"//div[@class='example']//div[3]//img[1]")
hover = ActionChains(driver).move_to_element(element3)
hover.perform()
time.sleep(2)

print("hovering complete")




