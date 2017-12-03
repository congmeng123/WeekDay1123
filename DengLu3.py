#javascript  是一门独立的语言
import time
from selenium import  webdriver
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get("http://172.31.6.158")

js = 'document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")'
driver.execute_script(js)
#点击登录
driver.find_element_by_link_text("登录").click()
#输入用户名密码
driver.find_element_by_id("username").send_keys("yonghuming ")
driver.find_element_by_id("password").send_keys("yonghuming")
time.sleep(2)
driver.find_element_by_class_name("login_btn").click()
time.sleep(6)
driver.find_element_by_css_selector("body > div.main.w1100 > div > div.content.fr > dl.dealing > dd > div > p > a").click()
