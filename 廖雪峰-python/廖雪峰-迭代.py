# -*- coding: utf-8 -*-
# -*- 迭代 dict 通过 for 循环 -*-
def die(val):
    for key in val:
        print(key)
# -*-  迭代 value -*-
def V(vals):
    for value in vals.values():
        print value
# -*- 同时迭代 key and value -*-
def duble(dub):
    for k, v in dub.items():
        print 'Key:', k
        print 'Value:', v

d = {'a': 1, 'b': 2, 'c': 3}
die(d)
V(d)
duble(d)
