#登录
import time
from  selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://172.31.6.105/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("yonghuming")
#
ActionChains(driver).send_keys(Keys.TAB).send_keys("yonghuming").send_keys(Keys.ENTER).perform()
driver.find_element_by_link_text("账号设置").click()
driver.find_element_by_partial_link_text("个人资料").click()
#修改个人信息
#每次send——keys之前都进行一遍clean操作
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("熊本熊")
#driver.find_element_by_css_selector('#xb[value="1"]').click()#男性别
driver.find_element_by_css_selector('[value="1"]').click()#男性别
#日历选择
#JavaScript是个单独语言，不能直接在pycharm中执行

# js ='document.getElementById("date").removeAttribute("readonly")'
# driver.execute_script(js)
# driver.find_element_by_id("date").clear()#首先清空之前的日期
# driver.find_element_by_id("date").send_keys("2017-11-25")
# time.sleep(2)
# driver.find_element_by_id("qq").send_keys("133423144")

#用arguements改写上面输入,用selenium定位方式之后，对元素执行JavaScript脚本，删除readonly属性
date = driver.find_element_by_id("date")
driver.execute_script('arguments[0].removeAttribute("readonly")',date)
date.clear()
date.send_keys("2017-11-11")
time.sleep(2)
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("1223344556")
# date = driver.execute_script("return document.getElementById('date')")
# #这句话等于  date = driver.findelement_bu_id("date)
# date.click()
driver.find_element_by_class_name("btn4").click()
#关闭弹出框,右键检查不了，叫做弹出框
time.sleep(3)
# driver.switch_to.alert.accept()#接受，同意
driver.switch_to.alert.dismiss()








