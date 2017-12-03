#导入pymysql代码库
import pymysql

#连接数据库
def connDb():
    #连接到数据库，需要知道数据库的IP，端口，用户名，密码，数据库名，，，
    conn = pymysql.Connect(host="localhost", user="root", password="root",database="pirate", port=3306,charset='utf8')
    #查询hd_user表中所有的数据，并且倒序打印
    sql = "select * from hd_user order by id desc"
    #要想在代码中执行这条sql语句，首先需要获取数据库的游标cyrsor
    curs = conn.cursor()
    #通过游标执行sql语句
    curs.execute(sql)
    #想获取数据库中最新的记录，fetchone()
    #那么就要把数据库所有记录倒序排列，然后用fetchone()获取第一条记录，即数据库最新的记录
    result = curs.fetchone()
    #conn.commit()增加，删除，修改只需要用commit就可以了
    #如果想获取所有的查询结果，fetchall()
    # result = curs.fetchall()
    return  result

if __name__ == '__main__':
    print(connDb())








