import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
time.sleep(1)

#infinite scroll function , we currently put a limit of 10 in order to stop it
def pageBottom(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    SCROLL_PAUSE_TIME = 0.5 
    n = 0
    while n<10:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        n+=1



driver.find_element(By.XPATH,"//a[normalize-space()='Infinite Scroll']").click()
time.sleep(1)
pageBottom(driver)


print("The Infinite loop is working correctly it has already ran 10 times so we stopped it")