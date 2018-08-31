# -*- coding: utf-8 -*-
__author__ = 'JetLi'


f = open('G:\\PyCharm\\untitled\\abd.txt', 'r')
print(f.read(9))
f.close()

with open('G:\\PyCharm\\untitled\\dfasdf.txt', 'r') as b:
    print(b.read())


a = open('G:\\PyCharm\\untitled\\abd.txt', 'r')
for line in a.readlines():
    print(line.strip())
a.close()

'''with open('G:\\PyCharm\\untitled\\abc.txt', 'w+') as d:
    d.write('你好吗aa？')
'''
with open('G:\\PyCharm\\untitled\\abd.txt', 'a+') as d:
    d.write('我爱你！')