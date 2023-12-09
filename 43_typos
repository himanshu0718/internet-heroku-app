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

driver.find_element(By.XPATH,"//a[normalize-space()='Typos']").click()
time.sleep(1)


typo_text = "Sometimes you'll see a typo, other times you won,t."
c = 0

for i in range(5):
    TEXT = driver.find_element(By.XPATH,"//p[2]").text 
    if TEXT == typo_text:
        # print("typo is present")
        c += 1
    else:
        pass
        # print("no typo present")
    driver.refresh()

print(f"Out of 5 times Typo error was present : {c} times")

