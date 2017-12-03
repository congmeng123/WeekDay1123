class PersonalCenterPage:
    #网页是基于浏览器的，不能在一个页面创建浏览器
    #应该把浏览器使用权。传进来就可以
    def __init__(self,driver):
        self.driver = driver

    title = "用户登录 - 道e坊商城 - Powered by Haidao"
