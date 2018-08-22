# -*- coding: utf-8 -*-
__author__ = 'JetLi'

"""__slots__核心作用是：可以在创建大量实例的时候更加节省内存。"""

"""正常情况下，当我们定义了一个 class，创建了一个 class 的实例后，我
们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定
义 class："""


class Student(object):
    def __init__(self):
        self.age = None

    pass


s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print s.name
# Michael

# 还可以尝试给实例绑定一个方法：


def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(22)
print s.age
# 22

s2 = Student()
# s2.set_age(22)
# AttributeError: 'Student' object has no attribute 'set_age'

# 为了给所有实例都绑定方法，可以给 class 绑定方法：


def set_score(self, score):  # 新建新方法
    self.score = score

Student.set_score = MethodType(set_score, Student)
# 给 class 绑定方法后，所有实例均可调用：
# for example:

s.set_score(100)
print s.score
# 100
s2.set_score(99)
print s2.score


"""通常情况下，上面的 set_score 方法可以直接定义在 class 中，但动态绑
定允许我们在程序运行的过程中动态给 class 加上功能，这在静态语言
中很难实现。"""

# -*- 使用 __slots__ -*-

"""但是，如果我们想要限制实例的属性怎么办？比如，只允许对 Student
实例添加 name 和 age 属性。"""


class Stu(object):
    __slots__ = ('addres', 'ages')

b = Stu()  # 创建新的实例
b.addres = 'Tom'  # 绑定属性'address'
b.ages = 101  # 绑定属性'ages'
# b.score = 90  # 绑定属性'score'
# AttributeError: 'Stu' object has no attribute 'score'

"""由于'score'没有被放到__slots__中，所以不能绑定 score 属性，试图绑
定 score 将得到 AttributeError 的错误。

使用__slots__要注意， __slots__定义的属性仅对当前类实例起作用，对
继承的子类是不起作用的："""
