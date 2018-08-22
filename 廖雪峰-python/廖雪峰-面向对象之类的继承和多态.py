# -*- coding: utf-8 -*-
"""在 OOP 程序设计中，当我们定义一个 class 的时候，可以从某个现有的
class 继承，新的 class 称为子类（Subclass），而被继承的 class 称为基
类、父类或超类（Base class、 Super class）。"""


class Animal(object):  # Animal 是两个子类 dog 和 cat 的父类
    def runs(self):
        print('Animal is running...')


"""当子类和父类都存在相同的 runs()方法时，我们说，子类的 runs()覆盖了
父类的 runs()，在代码运行的时候，总是会调用子类的 runs()。这样，我
们就获得了继承的另一个好处：多态。"""


# 也可以对子类增加一些方法，比如 Dog 类：
class dog(Animal):  # 子类 dog 继承了 父类Animal 的方法 runs()
    def runs(self):
        print('Dog is running...')


class cat(Animal):  # 子类 cat 继承了 父类Animal 的方法 runs()
    def runs(self):
        print('Cat is running...')


d = dog()
d.runs()
c = cat()
c.runs()

"""多态"""
"""当我们定义
一个 class 的时候，我们实际上就定义了一种数据类型。我们定义的数
据类型和 Python 自带的数据类型，比如 str、 list、 dict 没什么两样："""

a = list()
print isinstance(a, list)  # True
b = Animal()
print isinstance(b, Animal)  # True
print isinstance(d, dog)  # True

"""在继承关系中，如果一个实例的数据类型是某个子类，那它的数
据类型也可以被看做是父类。"""
print isinstance(c, cat)  # True
print isinstance(c, Animal)