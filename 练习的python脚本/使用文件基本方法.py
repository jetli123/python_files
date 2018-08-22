# -*- coding: utf-8 -*-

f = open(r'D:/Python27/python file/abd.txt')
lins = f.readlines()
f.close()
# lins[1] = 'It\'s not a\n'
# print lins
# c = open(r'G:\\PyCharm\\untitled\\abd.txt', 'w')
# c.writelines(lins)
# c.close()

def process(string):
    print 'Process: ', string


e = open(r'D:/Python27/python file/abd.txt')
while True:
    char = e.read(2)
    if not char:
        break
    process(char)
e.close()

d = open(r'D:/Python27/python file/abd.txt')
while True:
    char = d.readline()
    if not char:
        break
    process(char)
d.close()
