# -*- coding: utf-8 -*-
__author__ = 'JetLi'

"""一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们
用 instance.method()来调用。"""
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。


class Student(object):

    def __init__(self, name):
        self.name = name

    def __call__(self):
        print 'My name is %s' % self.name

s = Student('Michael')
s()  # # self 参数不要传入

# 判断一个变量是对象还是函数
# 判断一个对象是否能被调用，能被调用的对象就是一个 Callable 对象，
# 比如函数和我们上面定义的带有__call__()的类实例：
print callable(Student('Michael'))
# True
print callable(max)
# True
