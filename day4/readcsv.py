#1、导入CSV包
import csv
#2、读取文件信息，首先知道文件的存放路径
path = r"C:\Users\CMeng\PycharmProjects\WeekDay11\data\member_info.csv"
#3、路径打开
file = open(path,'r')
#4、通过csv代码库，读取csv格式的内容
data_table = csv.reader(file)
#5、
for row in data_table:
    print(row)