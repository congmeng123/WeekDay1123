#测试框架
#导入unittest框架
import  unittest
class UnittestDemo(unittest.TestCase):
    def setUp(self):
        print("这个方法会在测试用例执行之前运行")
    def tearDown(self):
        print("这个方法在测试用例方法之后运行")

# 4、编写测试用例方法
    def test_log_in(self):
        print("登录测试用例")
        self.zhu_ce()
    def zhu_ce(self):
        print("注册测试用例")

    def test_search(self):
        print("搜索测试用例")


if __name__ == '__main__':
    #执行当前文件中所有的unittest的测试用例
   #unittest.main()
    UnittestDemo().zhu_ce()
