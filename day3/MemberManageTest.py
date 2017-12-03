import unittest
import time
from selenium import webdriver

class MemberManageTest(unittest.TestCase):
    #变量前面加上self.表示这个变量是类的属性，可以被所有的方法访问
    def setUp(self):
        #打开浏览器
        #driver声命在setup方法之内，不能被其他方法访问
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()#浏览器升级就是注释掉这一行

    def tearDown(self):
        #quit()退出整个浏览器
        #close（）关闭一个浏览器
        #代码编写和调试的时候，需要在quit（）方法前加一个时间等待
        #正式运行的时候去掉时间等待，为了提高程序执行速度
        time.sleep(20)
        self.driver.quit()

    def test_add_member(self):
        #self.driver.get("")
        driver = self.driver
        driver.get("http://172.31.6.111/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        time.sleep(2)#mima
        driver.find_element_by_name("userpass").send_keys("password")
        time.sleep(1)#yanzhengma
        driver.find_element_by_name("userverify").send_keys("1234")
        #点击登录
        driver.find_element_by_css_selector("body > div.main > div > div.right > form > p:nth-child(4) > input").click()
        time.sleep(3)#点击会员管理
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/a[4]").click()
        time.sleep(2)#点击添加会员
        driver.switch_to.frame("mainFrame")
        # driver.find_element_by_xpath('//*[@id="addrow"]/span/span[1]').click()点击添加按钮
        driver.find_element_by_xpath("/html/body/div[2]/ul[1]/li[3]/a").click()
        time.sleep(4)
        #用户名
        driver.switch_to.frame("mainFrame")
        driver.find_element_by_name("username").send_keys("cong")
        time.sleep(2)
        driver.find_element_by_name("mobile_phone").send_keys("15727395979")
        time.sleep(2)
