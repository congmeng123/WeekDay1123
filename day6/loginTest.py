import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from day5.myTestCase import MyTestCase
from day6.page_oobject.loginPage import LoginPage
from day6.page_oobject.personalCenterPage import PersonalCenterPage


class LoginTest(MyTestCase):
    def test_login(self):
        #打开网页
        #self.driver.get("http://172.31.6.158/index.php?m=user&c=public&a=login")
        lp = LoginPage(self.driver)#实例化一个登录页面
        lp.open()
        #输入用户名
        # self.driver.find_element(By.ID,"username").send_keys("yonghuming")
        lp.input_username("yonghuming")
        time.sleep(1)
        #输入密码
        # self.driver.find_element(By.ID,"password")
        lp.input_password("yonghuming")
        time.sleep(1)
        #点击登录按钮
        # self.driver.find_element(By.CLASS_NAME,"login_btn")
        lp.click_login_button()
        #验证是否跳转到管理中心页面
        # expected = "我的会员中心 - 道e坊商城 - Powered by Haidao"
        # time.sleep(3)
        # self.assertIn("我的会员中心",self.driver.title)
        pcp = PersonalCenterPage(self.driver)
        time.sleep(2)
        self.assertEqual(pcp.title, self.driver.title)
















