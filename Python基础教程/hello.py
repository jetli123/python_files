# -*- coding: utf-8 -*-
__author__ = 'JetLi'

"""动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定
义的，而是运行时动态创建的"""


class Hello(object):
    @staticmethod
    def hello(name='world'):
        print 'Hello, %s.' % name
"""要创建一个 class 对象， type()函数依次传入 3 个参数：
1. class 的名称；
2. 继承的父类集合，注意 Python 支持多重继承，如果只有一个父类，
别忘了 tuple 的单元素写法；
3. class 的方法名称与函数绑定，这里我们把函数 fn 绑定到方法名
hello 上。

通过 type()函数创建的类和直接写 class 是完全一样的，因为 Python 解
释器遇到 class 定义时，仅仅是扫描一下 class 定义的语法，然后调用 type()
函数创建出 class。"""


def fn(self, name='world'):
    print 'Hello, %s!' % name

She = type('Hello', (object,), dict(hello=fn))
h = She()
h.hello()
print type(She)
print type(h)