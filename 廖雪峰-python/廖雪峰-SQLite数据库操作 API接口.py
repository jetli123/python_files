# -*- coding: utf-8 -*-
"""
要操作关系数据库，首先需要连接到数据库，一个数据库连接称为
Connection；
连接到数据库后，需要打开游标，称之为 Cursor，通过 Cursor 执行 SQL
语句，然后，获得执行结果。
"""
"""由于 SQLite 的驱动内置在 Python 标准库中，所以我们可以直接来操作
SQLite 数据库。"""
# 导入 SQLite 驱动:
import sqlite3

# 连接到 SQLite 数据库
# 数据库文件是 test.db
# 如果文件不存在，会自动在当前目录创建:\
conn = sqlite3.connect('test.db')
# 创建一个 Cursor:
cursor = conn.cursor()
try:
    # 执行一条 SQL 语句，创建 user 表:
    # cursor.execute('create table user1 (id varchar(5) primary key, name varchar(20))')
    # 继续执行一条 SQL 语句，插入一条记录:
    cursor.execute('insert into user1 (id, name) values (\'6\', \'Jam\')')
# 通过 rowcount 获得插入的行数:
    print cursor.rowcount
# 关闭 Cursor:
except StandardError as e:
    print 'StandardError:', e
finally:
    cursor.close()
# 提交事务:
    conn.commit()
# 关闭 Connection:
    conn.close()

"""我们再试试查询记录："""
conn1 = sqlite3.connect('test.db')
cursor1 = conn1.cursor()
try:
    # 执行查询语句:
    cursor1.execute('select * from user1 where id=?', '6')
# 获得查询结果集:
    values = cursor1.fetchall()
    print values
except StandardError as b:
    print 'StandardError: ', b
finally:
    cursor1.close()
    conn1.close()


"""小结"""
# 使用 Cursor 对象执行 insert， update， delete 语句时，执行结果由 rowcount
# 返回影响的行数，就可以拿到执行结果。
# 使用 Cursor 对象执行 select 语句时，通过 featchall()可以拿到结果集。
# 结果集是一个 list，每个元素都是一个 tuple，对应一行记录。
# 如果 SQL 语句带有参数，那么需要把参数按照位置传递给 execute()方
# 法，有几个?占位符就必须对应几个参数，例如：
# cursor.execute('select * from user where id=?', '1')
