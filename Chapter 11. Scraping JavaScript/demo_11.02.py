from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException

def waitForLoad(driver):
    element = driver.find_element_by_tag_name('html')
    cnt = 0
    
    while True:
        cnt += 1
        
        if cnt > 20:
            print(f"=>> Hết thời gian sau 10s và quay trở lại.")
            return
        
        time.sleep(.5)
        try:
            element == driver.find_element_by_tag_name('html')
        except StaleElementReferenceException:
            return
        
driver = webdriver.PhantomJS()
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
waitForLoad(driver)
print(driver.page_source)