import csv
import os
def read(file_name):
    #所有的重复代码的出现都是程序设置得不合理，重复代码应该封装在一个方法里
    current_file_path = os.path.dirname(__file__)
    path = current_file_path.replace("day4", "data/" + file_name)
    # file = open(path,'r')  #with语句是一个代码块，代码块中的内容都要缩进4个空格
    #with代码块可以自动关闭with中声明的变量file
    #因为file文件一旦被关闭，里面的数据也随着消失，单一单独声明一个列表result，来保存里面的数据
    result = []
    with open(path,'r') as file:
        data_table=csv.reader(file)
        for row in data_table:
            result.append(row)
    return result

    #如果在打开和关闭程序之间，发生了异常情况，导致后面的代码不能正常运行
    #file.close()也不能执行，文件又会不能关闭，应该用with  as 语句实现
    file.close()#关闭

if __name__ == '__main__':
    # path = r"C:\Users\CMeng\PycharmProjects\WeekDay11\data\member_info.csv"
    #这个路径是一个绝对路径，需要设置自动找到路径.os就是操作系统,file是双下划线
    # current_file_path = os.path.dirname(__file__)
    #print(current_file_path)打印上面路径，真正想要的路径是sv
    # path = current_file_path.replace("day4","data/member_info.csv")
    # print(path)
    member_info =read("member_info.csv")
    # print(member_info) 这个一行显示
    for row in member_info:
        print(row[4])#加[]就可以单独打印那一列
    #5、读出数据不是目的，目的是通过这些数据驱动测试

