# -*- coding: utf-8 -*-
"""把变量从内存中变成可存储或传输的过程称之为序列化

在 Python中叫 pickling
序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到
别的机器上。
"""
import pickle

# 我们尝试把一个对象序列化并写入文件

# 方法1： 将对象序列化成bytes 写入文件中 使用 pickle.dumps() 函数
d = dict(name='Jet', age=20, score=88)
c = pickle.dumps(d)  # pickle.dumps()方法把任意对象序列化成一个 bytes，然后，就可以把这个 bytes 写入文件
a = open('D:/Python27/python file/fff.txt', 'wb')
a.write(c)
a.close()
'''
# 方法2： 直接把对象序列化后写入一个 file-like Object 使用 pickle.dump() 函数
d1 = dict(name='Jet', age=20, score=88)
f = open('D:/Python27/python file/ff1.txt', 'wb')
pickle.dump(d1, f)
f.close()

# 方法3： with 方法写入文件，自动关闭
d2 = dict(name='Jet', age=20, score=88)
with open('D:/Python27/python file/ff2.txt', 'wb') as f:
    pickle.dump(d2, f)

# 把对象从磁盘读到内存时，可以先把内容读到一个 bytes，然
# 后用 pickle.loads()方法反序列化出对象，也可以直接用 pickle.load()
# 方法从一个 file-like Object 中直接反序列化出对象

# 方法1： read() 方法读到文件中的 bytes，用pickle.loads() 方法反序列化
n = open('D:/Python27/python file/ff1.txt', 'rb')
b = n.read()
print pickle.loads(b)  # pickle.loads(n.read())
n.close()

# 方法2： 打开文件，直接用 pickle.load() 方法反序列化出对象
m = open('D:/Python27/python file/ff2.txt', 'rb')
print pickle.load(m)
m.close()
'''