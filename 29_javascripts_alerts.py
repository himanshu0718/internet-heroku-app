import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains


driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH,"//a[text()='JavaScript Alerts']").click()
time.sleep(1)

#js alert
driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
time.sleep(1)
alert_obj = driver.switch_to.alert
alert_obj.accept()
time.sleep(1)

js_alert_text = driver.find_element(By.XPATH,"//p[@id='result']").text
print(js_alert_text)

#js confirm alert 
#ok
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']").click()
time.sleep(1)
alert_obj = driver.switch_to.alert
alert_obj.accept()
js_confirm_ok_text = driver.find_element(By.XPATH,"//p[@id='result']").text
print(js_confirm_ok_text)

#cancel
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']").click()
time.sleep(1)
alert_obj = driver.switch_to.alert
alert_obj.dismiss()
js_confirm_cancel_text = driver.find_element(By.XPATH,"//p[@id='result']").text
print(js_confirm_cancel_text)

#js prompt
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(1)
alert_obj = driver.switch_to.alert
alert_obj.send_keys("Hello World")
time.sleep(1)
alert_obj.accept()
time.sleep(1)
js_prompt_text = driver.find_element(By.XPATH,"//p[@id='result']").text
print(js_prompt_text)
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
alert_obj.send_keys("Hello")
alert_obj = driver.switch_to.alert
alert_obj.dismiss()
time.sleep(1)
js_prompt_cancel = driver.find_element(By.XPATH,"//p[@id='result']").text
print(js_prompt_cancel)













