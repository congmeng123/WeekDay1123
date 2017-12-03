import unittest
import time
from selenium import webdriver

class DengLuTest(unittest.TestCase):
    """登陆模块测试用例"""

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(20)
        self.driver.quit()

    def test_denglu(self):
        """登陆模块正常测试用例"""
        driver=self.driver
        driver.get("http://172.31.6.158/index.php?m=user&c=public&a=login")
        time.sleep(2)
        driver.find_element_by_id("username").send_keys("yonghuming")
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("yonghuming")
        time.sleep(2)
        driver.find_element_by_class_name("login_btn").click()
        print("0_0")