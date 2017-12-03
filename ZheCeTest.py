import time
#打开浏览器
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
time.sleep(3)
#打开商城
driver.get("http://172.31.6.64")
time.sleep(2)
#点击注册链接
#第四种定位方法：链接的文本信息
driver.find_element_by_link_text("注册").click()
time.sleep(2)
#窗口切换：把selenium切换到新的窗口工作
cwh = driver.current_window_handle # 浏览器当前窗口的句柄，handle 把手的意思
#print(cwh)可以将cwh的值打印出来
#selenium只提供了selenium工作窗口的名字，并没有提供第二个窗口的名字，需要自己求
whs = driver.window_handles #浏览器中所有的窗口句柄
# for关键字（类型名 变量名 ：数组）{}
# for 关键字 _ 集合中的某个元素  in 关键字 数组/集合  冒号
# 所以item 表示whs中的一个元素，每次循环取一个值，循环结束。whs中每个元素都会被遍历一次
#Python语法：遇到冒号，下一行，肯定要空 4 格，格式严格
# 和for循环缩进程度一样，表示循环外面的代码
#for 循环里面的代码必须多缩进4个空格
for item in whs:
    if item ==cwh:
        driver.close()#关闭当前标签
    else:#这种情况，item 就是我们要找的窗口
        driver.switch_to.window(item)
#4、输入用户信息
driver.find_element_by_name("username").send_keys("cong1118")
time.sleep(2)
driver.find_element_by_name("password").send_keys("cong1118")
time.sleep(2)
driver.find_element_by_name("userpassword2").send_keys("cong1118")
time.sleep(2)
driver.find_element_by_name("mobile_phone").send_keys("15727395979")


















