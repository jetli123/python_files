# -*- coding: utf-8 -*-

f = open(r'D:/Python27/python file/abc.txt', 'w')
f.write('01234567890123456789')
f.seek(-2, 2)
f.write('Hello, world!')
f.close()

with open(r'D:/Python27/python file/abc.txt') as f:
    print f.read()

c = open(r'D:/Python27/python file/abc.txt')
print c.read(11)  # 读取11个字节
print c.read(5)  # 继续读取5个 字节
print c.tell()  # 现在文件指针所在的位置
c.close()

a = open(r'D:/Python27/python file/abd.txt')
b = 1
for i in range(4):
    print str(b) + ': ' + a.readline()
    b += 1
a.close()
