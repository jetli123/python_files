# -*- coding: utf-8 -*-
"""文件迭代器"""
import sys


def process(string):
    print('Process: ', string)


f = open(r'G:\\PyCharm\\untitled\\abd.txt')  # 迭代文件
for line in f:
    process(line)
f.close()

# 例子2
# 对文件进行迭代，而不使用变量存储文件对象
for line in open('G:\\PyCharm\\untitled\\abd.txt'):
    process(line)

for line in sys.stdin:
    process(line)
