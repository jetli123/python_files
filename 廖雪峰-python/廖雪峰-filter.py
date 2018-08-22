# -*- coding: utf-8 -*-
# -*- filter()也接收一个函数和一个序列
# -*- filter()把传入的函数依次作用于每个元素，然后根据返回值是 True 还是 False 决定保留还是丢弃该元素
# 在一个 list 中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return n % 2 == 1

print list(filter(is_odd, [1, 2, 4, 7, 9, 8, 10, 15]))

# -*- 把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()

print list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))