from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://srgoc.org/SRCEM%20about.htm")
print(driver.title)
time.sleep(2)
class="search-field" placeholder="search" value=""  name="s"
var = driver.find_element_by_class_name("search_field")
var2 = driver.find_element_by_name("s")
print(var.is_display())
print(var2.is_enable())
# print(var.is_select())
driver.close()