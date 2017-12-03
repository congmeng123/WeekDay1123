from selenium.webdriver.common.by import By
class LoginPage:
    # 构造方法的作用
    # 实例化LoginPage对象的时候，必须要构造方法，（固定写法）
    # python中构造方法是固定写法：__init__表示构造方法
    # 需要把driver作为参数传进来
    # 方便别的属性和方法使用driver
    def __init__(self,driver):
        self.driver = driver
    title = "用户名 - 道e坊商城 -Powered by Haidao"
    url = "http://172.31.6.158/index.php?m=user&c=public&a=login"
    #小括号表示元组，元素中有2个值，第一个是控件的定位方式，第二个是控件定位方式的具体值
    username_input_loc = (By.ID,"username")
    password_input_loc = (By.ID,"password")
    login_button_loc = (By.CLASS_NAME,"login_btn")

    def click_login_button(self):
        self.driver.find_element(*self.login_button_loc).click()

    def open(self):
        self.driver.get(self.url)

    def input_username(self,username):
        # self.driver.find_element_by_id("username").send_keys("yonghuming")
        # self.driver.find_element_by_id("password").send_keys("yonghuming")
        #*的作用，表示把一个元组中的元素分别传入方法列表参数中
        #前面加一个星号，表示传入就不是元组，而是元组中两个元素
        self.driver.find_element(*self.username_input_loc).send_keys(username)

    def input_password(self,password):
        self.driver.find_element(*self.password_input_loc).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button_loc).click()


