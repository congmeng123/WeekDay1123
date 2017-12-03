import unittest

import time
from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from day4.readCsv2 import read


class MemberManageTest(unittest.TestCase):

    ##在当前类只执行一次
    @classmethod
    def setUpClass(cls):
        print("所有方法之前，执行一次")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)#20s后关闭
        # cls.driver.close()

    def test_a_log_in(self): #ab是执行顺序
        print("登录测试")
        driver = self.driver
        driver.get("http://172.31.6.105/admin.php")
        driver.find_element_by_name("username").send_keys("admin")
        ActionChains(driver).send_keys(Keys.TAB).send_keys("password").send_keys(Keys.TAB).send_keys("1234").send_keys(Keys.ENTER).perform()


    def test_b_add_member(self):
        for row in read("member_info.csv"):
            print("添加会员")
            driver = self.driver
            driver.find_element_by_link_text("会员管理").click()
            driver.find_element_by_link_text("添加会员").click()
            #如果frame没有name属性时，可以通过其他方式定位iframe标签，把定位好的页面传给driver.switch_to.frame(iframe_html)方法也可以实现frame切换
            iframe_css = "#mainFrame"
            iframe_html = driver.find_element_by_css_selector(iframe_css)
            driver.switch_to.frame(iframe_html)
            driver.find_element_by_name("username").send_keys(row[0])
            time.sleep(1)
            driver.find_element_by_name("mobile_phone").send_keys(row[1])
            time.sleep(1)
            driver.find_element_by_css_selector('[value=[]]').click()


            #切换到父框架
            # driver.switch_to.parent_frame()
            #切换到网页的根节点，（用一个就行）
            driver.switch_to.default_content()
            # driver.find_element_by_name("username").send_keys("大熊")
            # time.sleep(2)
            # driver.find_element_by_name("mobile_phone").send_keys("15727395939")


if __name__ == '__main__':
        unittest.main()#鼠标移动到这里运行就可以了

