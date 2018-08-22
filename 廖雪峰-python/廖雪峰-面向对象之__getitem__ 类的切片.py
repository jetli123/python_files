# -*- coding: utf-8 -*-
"""要表现得像 list 那样按照下标取出元素，需要实现__getitem__()方法"""


class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f = Fib()
print f[0], f[5]

# 但是 list 有个神奇的切片方法：
# >>> list(range(100))[5:10]
# [5, 6, 7, 8, 9]
# 对于 Fib 却报错。原因是__getitem__()传入的参数可能是一个 int，也可能是一个切片对象 slice，所以要做判断：


class FIb(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
d = FIb()
print d[1:5]
