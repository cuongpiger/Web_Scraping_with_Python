from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")

try:
    body_elem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//body[contains(text(), "This is the page you are looking for!")]')))

    print(body_elem.text)
except TimeoutException:
    print("Ko tìm thấy element body này!")