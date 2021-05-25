import pymssql
import pandas as pd
def link():
    conn = pymssql.connect(database='Wine', charset='utf8')
    return conn

def search():
    conn=link()
    cursor = conn.cursor()
    cursor.execute("select * from wine")
    cursor.fetchall()
    print('共查询到：', cursor.rowcount, '条数据。')
    # 输出全部并用pandas处理
    st = pd.read_sql('''select * from wine''', conn)
    print(st)
    close(cursor, conn)


def add():
    conn = link()
    cursor = conn.cursor()
    sql = "insert into wine values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"  # 注意是%s,不是s%
    data = ('4'	,'12.63',	'3.6'	,'2.3'	,'20.1'	,'99',	'2.06',	'0.69',	'0.46'	,'1.06'	,'6.9',	'0.65',	'1.4'	,'666')
    cursor.execute(sql, data)
    conn.commit()   # 提交
    cursor.execute("select * from wine")
    cursor.fetchall()
    print('增加数据后共查询到：', cursor.rowcount, '条数据。')
    close(cursor, conn)

def avgProline():
    conn = link()
    cursor = conn.cursor()
    # 统计 脯氨酸 ‘Proline’均值
    avg=0
    st = pd.read_sql('''select * from wine''', conn)
    for i in st['Proline']:
        avg+=i
    print('‘Proline’均值:'+str(avg/len(st['Proline'])))
    close(cursor, conn)

def delete():

    conn = link()
    cursor = conn.cursor()
    cursor.execute("delete  from wine")
    close(cursor, conn)

def close(cursor,conn):
    cursor.close()  # 关闭游标
    conn.close()  # 关闭连接

if __name__ == '__main__':
    search()
    add()
    avgProline()
    # delete()