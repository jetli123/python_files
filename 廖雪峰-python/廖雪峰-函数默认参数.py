# -*- coding: utf-8 -*-
# -*- 计算 x^2 函数 -*-
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
