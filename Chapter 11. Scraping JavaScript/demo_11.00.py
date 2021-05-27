from selenium import webdriver
import time

driver = webdriver.PhantomJS()
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3) # tạm dừng 3 giây

print("_________________________________________________")
print(driver.find_element_by_id('content').text)
driver.close()