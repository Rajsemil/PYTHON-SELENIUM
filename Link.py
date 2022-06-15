from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://srgoc.org/SRCEM%20about.htm")
# link name
link = driver.find_element(By.TAG_NAME,"a")
# link text
link = driver.find_element(By.LINK_TEXT,"Home")
# Partial link text
# same to link text

