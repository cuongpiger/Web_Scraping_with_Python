from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.PhantomJS()
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')

try:
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'loadedButton'))) # loadedButton là id của cái button trên web đó, inspect mà coi, dòng này có nghĩa là chờ cho cái button này hiện lên
finally:
    print('_____________________________________________________')
    print(driver.find_element(By.ID, 'content').text)
    driver.close()