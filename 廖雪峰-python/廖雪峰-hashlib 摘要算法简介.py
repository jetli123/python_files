# -*- coding: utf-8 -*-
"""
    摘要算法又称哈希算法、 散列算法。它通过一个函
数，把任意长度的数据转换为一个长度固定的数据串（通常用 16 进制
的字符串表示）。
"""
import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# 如果数据量很大，可以分块多次调用 update()，最后计算的结果是一样
md5.update('python hashlib?'.encode('utf-8'))
md5.update('Yes, I do!'.encode('utf-8'))
print md5.hexdigest()
# eab4298fa328eddcb34e2e5dfe1f1a73
