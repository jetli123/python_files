# -*- coding: utf-8 -*-
import os
import sqlite3

# 初始化数据库
# df_file = os.path.join(os.path.dirname('G:\\PyCharm\\untitled\\'), 'test.db')
# if os.path.isfile(df_file):
#     os.remove(df_file)

# 初始化数据
conn = sqlite3.connect('test.db')
cursor = conn.cursor()  # 创建一个 Cursor: 为了执行sql 语句
try:
    cursor.execute('create table user(id varchar(10) primary key, name varchar(20), score int)')
    cursor.execute(r"insert into user values('A-001','Adam',95)")
    cursor.execute(r"insert into user values('A-002', 'Bart', 62)")
    cursor.execute(r"insert into user values('A-003', 'Lisa', 78)")
except StandardError as e:
    assert isinstance(e, object)
    print('StandardError: ', e)
finally:
    cursor.close()  # 关闭游标
    conn.commit()  # 提交事物
    conn.close()  # 关闭数据库

def get_score_in(low, high):
    conn1 = sqlite3.connect('test.db')
    cursor1 = conn1.cursor()
    try:
        cursor1.execute(r"select name from user where score between %d and %d order by score" % (low, high))
        value = cursor1.fetchall()
        return value
    except StandardError as f:
        print('StandardError: ', f)
    finally:
        cursor1.close()
        conn1.close()

if __name__ == '__main__':
    print(get_score_in(60, 80))
