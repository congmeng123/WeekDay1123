import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://172.31.6.158/index.php?m=user&c=public&a=login")
time.sleep(2)
driver.find_element_by_id("username").send_keys("yonghuming")
time.sleep(2)
driver.find_element_by_id("password").send_keys("yonghuming")
#如果使用方法，没有提示信息就是错误的
time.sleep(2)
driver.find_element_by_class_name("login_btn").click()
