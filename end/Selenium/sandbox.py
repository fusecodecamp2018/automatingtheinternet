from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)
driver.switch_to_window(driver.current_window_handle)
driver.get("http://www.python.org")
time.sleep(2)
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
time.sleep(2)
assert "No results found." not in driver.page_source
time.sleep(5)
driver.close()
