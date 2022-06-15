from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://srgoc.org/SRCEM%20about.htm")
driver.find_element_by_xpath("//*[@ID=html9]/DIV[1]/BUTTON").click()
time.sleep(2)
driver.switch_to_alert().eccept()
time.sleep(2)
driver.switch().dismiss()
time.sleep()