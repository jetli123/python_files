# -*- coding: utf-8 -*-
"""当调用不存在的属性时，比如 score， Python 解释器会试图调用
__getattr__(
self, 'score')来尝试获得属性，这样，我们就有机会返回
score 的值"""
"""注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，
比如 name，不会在__getattr__中查找。"""


class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99


s = Student()
print s.name
# Michael
print s.score


# 99

# 返回函数也是完全可以的：


class Stu(object):
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25


b = Stu()
print b.age()
# 25
print b.name
# None

"""此外，注意到任意调用如 s.abc 都会返回 None，这是因为我们定义的
__getattr__默认返回就是 None。要让 class 只响应特定的几个属性，我
们就要按照约定，抛出 AttributeError 的错误："""


class Students(object):
    def __getattr__(self, attr):
        if attr == 'ages':
            return lambda: 22
        raise AttributeError('\'Students \' object has no attribute \'%s\'' % attr)


c = Students()
print c.ages()
# 22
print c.name()


class Chain(object):
    def __init__(self, path=''):
        self.path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


Chain().stauts.user.timeline.list

