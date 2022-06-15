from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://srgoc.org/SRCEM%20about.htm")
#print(driver.title)
time.sleep(5)
driver.maximize_window()
driver.minimize_window()
driver.quit()