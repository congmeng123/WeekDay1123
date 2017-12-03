import time
from tkinter.tix import Select

from selenium import  webdriver
#firefox浏览器的45版本一下的
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
#driver = webdriver.Firefox()45版本需要驱动，以下不需要驱动
driver.get("http://172.31.6.64")
#点击登陆之前先，删除target属性，但是JavaScript定位比较麻烦，可以用selenium定位方式代替JavaScript的定位方式，用argument关键字
login_link = driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
driver.find_element_by_id("username").send_keys("yonghuming")
time.sleep(2)
driver.find_element_by_id("password").send_keys("yonghuming")
time.sleep(2)
driver.find_element_by_id("password").submit()
driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
driver.find_element_by_css_selector("div:nth-child(2) > div.shop_01-imgbox > a > img").click()
#driver.execute_script("arguments[0].removeAttribute('target')",iphone_link2)
cu = driver.current_window_handle
wh = driver.window_handles
for item in wh:
    if item in cu:
        driver.close()
    else:
        driver.switch_to.window(item)
driver.find_element_by_id("joinCarButton").click()
#点击加入购物车按钮
driver.find_element_by_css_selector("div.shopCar_T > span.shopCar_T_span3").click()
#点击去购物车结算
driver.find_element_by_css_selector("div:nth-child(4) > div:nth-child(3) > a").click()
#点击结算
#添加新地址
driver.find_element_by_css_selector("#address-box > div").click()
time.sleep(2)
#填写收货人
driver.find_element_by_name("address[address_name]").send_keys("收获人")
driver.find_element_by_name("address[mobile]").send_keys("15727394959")
#选择下拉框
#driver.find_element_by_id("add-new-area-select")
#driver.find_element_by_css_selector("[value='370000']").click()
#定义第一个下拉框
sheng = driver.find_element_by_id("add-new-area-select").click()
Select(sheng).select_by_value('460000')

#定位第二个下框
shi = driver.find_element_by_tag_name("select")[1]
Select(shi).select_by_index(2)

#定位第三个下拉框
xian = driver.find_element_by_tag_name("select")[2]
Select(xian).select_by_visible_text("东城区")
# driver.find_element_by_css_selector("[value='370200']").click()
# time.sleep(2)
# driver.find_element_by_css_selector("[value='370212']").click()
# time.sleep(2)
# driver.find_element_by_name("address[address]").send_keys("崂山公交站119路")
# time.sleep(2)
# driver.find_element_by_name("address[zipcode]").send_keys("262700")
# time.sleep(2)
# driver.find_element_by_class_name("aui_state_highlight").click()





