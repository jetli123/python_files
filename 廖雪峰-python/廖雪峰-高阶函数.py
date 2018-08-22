# -*- coding: utf-8 -*-
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以
# 接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(x, y, f):
    return f(x) + f(y)

print add(-2, -4, abs)