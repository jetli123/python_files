# -*- coding: utf-8 -*-
"""
由于 MySQL 服务器以独立的进程运行，并通过网络对外服务，所以，
需要支持 Python 的 MySQL 驱动来连接到 MySQL 服务器。MySQL 官
方提供了 mysql-connector-python 驱动，但是安装的时候需要给 pip 命令
加上参数--allow-external：
$ pip install mysql-connector-python --allow-external

"""
# 导入 MySQL 驱动:
import mysql.connector

# 注意把 password 设为你的 root 口令:
conn = mysql.connector.connect(user='root', password='mysql', host='localhost', database='test')
cursor = conn.cursor()
try:
    # 创建 user 表:
    # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    # 插入一行记录，注意 MySQL 的占位符是%s:
    cursor.execute('insert into user (id, name) values (%s, %s)', ['12', 'Oracles'])
    cursor.execute('insert into user values(%s, %s)', ['13', 'JetLIs'])
    cursor.execute('insert into user values(%s, %s)', ['14', 'Mysqls'])
    print cursor.rowcount
except mysql.connector.errors.IntegrityError as e:
    print 'MySQL Error: ', e
finally:
    conn.commit()  # 提交事务:
    cursor.close()
    conn.close()
# 运行查询:
# cursor1 = conn.cursor()
# cursor1.execute('select * from user where id = %s', ['1'])
# values = cursor1.fetchall()
# print values

# 关闭 Cursor 和 Connection:
# cursor1.close()
# conn.close()
