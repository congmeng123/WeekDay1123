import os
import smtplib
import unittest
#HTMLTestRunner基于unnittest框架的一个扩展，可以自己在网上下载
import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner

def send_mail(path):
    f=open(path,'rb')
    mail_boy=f.read()
    f.close()

    #要想发邮件，我们要把二进制的内容转成MIME格式
    #MIME 多用途互联网邮件扩展
    #这种格式是对邮件协议的一个扩展，使邮件不仅支持文本格式，还支持多种格式
    msg=MIMEText(mail_boy,'html','utf-8')
    #上边是邮寄的正文，但是对于一个邮件来讲，除了正文，还需要主题，发件人，收件人
    #msg是字典的类型，字典类似于数组，区别是1，字典是无序的
    #
    msg['Subject']=Header("自动化测试报告￥￥￥￥",'utf-8')
    #如果想用客户端软件或者自己写代码登陆邮箱，很多邮箱的服务器是需要单独设置一个客户端的授权码
    #为了邮箱的安全
    msg['From']="15717395939@163.com"
    msg['To']="1334395614@qq.com"

    #邮件内容已经准备好了，下面开始发送邮件
    #发邮件的手动步骤
    #1，打开登录页面，链接邮箱服务器
    #要想链接服务器，首先必须搞清楚网络传输协议
    #http，https，ftp,socket
    #发邮件的协议，必须有三种，你要先查看你的邮箱支持哪种协议
    #pop3，smtp，imap
    #我们需要选一种传输协议用来发邮件
    #smtp simple mail transful protocol简单邮件传输协议
    #首先导入smpilib的代码库
    smtp=smtplib.SMTP()#实例化一个类的对象
    smtp.connect("smtp.163.com") #链接126邮箱的，服务器的地址
    #2，登陆邮箱
    smtp.login('15727395939@163.com','1qaz!QAZ')
    #3，发送邮件
    smtp.sendmail("15727395939@163.com","1334395614@qq.com", msg.as_string())
    #4，退出邮箱
    smtp.quit()
    print("邮件发送成功***********")

if __name__ == '__main__':
    #str是string f是format格式
    #strftime（）通过这个方法可以定义时间的格式
    now=time.strftime("%Y-%m-%d_%H-%M-%S")

    suite=unittest.defaultTestLoader.discover('./day5','*Test.py')
    #unittest.TextTestRunner()文本测试用例运行器
    #现在用html测试用例运行器最终会生成一个html格式的测试报告
    #指定测试报告的路径
    #当前路径
    base_path=os.path.dirname(__file__)
    path=base_path+"/report/report" + now + ".html"
    file=open(path,'wb')
    HTMLTestRunner(stream=file,title="海盗商城的测试报告abc", description="测试环境window sever2008+Chrome").run(suite)
    file.close()
    #我们要把html报告作为邮件正文，发邮件
    send_mail(path)
    #这时生成的测试报告，只显示类名和方法名，只能给专业的人使用
    #我们应该相关的手动测试用例的标题加到我们的测试报告
    #我们自动化测试用例是从手工测试用例挑出来的，手工测试用例怎么写，我们就怎么编码
    #所以我们的代码里应该体现手工测试用例的标题
    #当测试用例全部执行完成我们应该生成一封提醒邮件，通知所有关心测试结果的人


