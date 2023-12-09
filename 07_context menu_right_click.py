import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
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

