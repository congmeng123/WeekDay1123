#打开
import time
from selenium import  webdriver
driver = webdriver.Chrome()
driver.get("http://172.31.6.158")
#登录
driver.find_element_by_link_text("登录").click()
time.sleep(2)
#从浏览器中的所有窗口中，排除第一个窗口
#把selenium切换到第二个窗口
cw = driver.current_window_handle
whs = driver.window_handles
#item 表示集合中的一个元素
for item in whs:
    if item == cw:
        driver.close()
    else:
        driver.switch_to.window(item)
#输入用户名
driver.find_element_by_id("username").send_keys("yonghuming")
time.sleep(2)
driver.find_element_by_id("password").send_keys("yonghuming")
#点击登录按钮
driver.find_element_by_class_name("login_btn").click()


