# -*- coding: utf-8 -*-
__author__ = 'JetLi'

# -*- __str__ -*-


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__  # 直接显示变量调用的不是__str__()，而是__repr__()，两者的
                        # 区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者
                        # 看到的字符串，也就是说， __repr__()是为调试服务的。

# 这样打印出来的实例，不但好看，而且容易看出实例内部重要的数据

print (Student('Michael'))  #  直接显示变量调用的 __str__()
s = Student('Michael')  # 直接显示变量调用的 __repr__()
print s
#################################################
#              -*- __iter__ -*-     ###########
"""如果一个类想被用于 for ... in 循环，类似 list 或 tuple 那样，就必须实
现一个__iter__()方法，该方法返回一个迭代对象，然后， Python 的 for
循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
直到遇到 StopIteration 错误时退出循环。"""

# 我们以斐波那契数列为例，写一个 Fib 类，可以作用于 for 循环


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器 a， b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def next(self):  # python 3.0 以上版本 用 __next__ 方法
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 1000:  # 退出循环条件
            raise StopIteration
        return self.a  # 返回下一个值


for n in Fib():
    assert isinstance(n, object)
    print n
