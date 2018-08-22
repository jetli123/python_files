# -*- coding: utf-8 -*-
__author__ = 'JetLi'

"""继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩
展父类的功能。"""

"""
Dog - 狗狗；
Bat - 蝙蝠；
Parrot - 鹦鹉；
Ostrich - 鸵鸟。

Mammal 哺乳类：能跑的哺乳类，能飞的哺乳类；
Bird 鸟类：能跑的鸟类，能飞的鸟类。
"""
# 采用多重继承。首先，主要的类层次仍按照哺乳类和鸟类设计


class Animal(object):
    pass


class Mammal(Animal):  # 大类
    pass


class Bird(Animal):  # 大类
    pass

"""现在，我们要给动物再加上 Runnable 和 Flyable 的功能，只需要先定义
好 Runnable 和 Flyable 的类："""


class RunnableMixin(object):
    @staticmethod
    def run():
        print 'Running...'


class FlyableMixin(object):
    @staticmethod
    def fly():
        print 'Flying...'


class Dog(Mammal, RunnableMixin):  # 对于需要 Runnable 功能的动物，就多继承一个 Runnable，例如 Dog
    pass


class Bat(Mammal, FlyableMixin):  # 对于需要 Flyable 功能的动物，就多继承一个 Flyable，例如 Bat：
    pass


class Parrot(Bird, FlyableMixin):
    pass


class Ostrich(Bird, RunnableMixin):
    pass


b = Bat()
b.fly()
c = Dog()
c.run()
d = Parrot()
d.fly()
e = Ostrich()
e.run()

"""如果需要“混入”额外的功能，通过多重继承就可以Python3 基础教程【完整版】 http://www.yeayee.com/
195/531
实现，比如，让 Ostrich 除了继承自 Bird 外，再同时继承 Runnable。这
种设计通常称之为 MixIn。"""

"""MixIn 的目的就是给一个类增加多个功能，这样，在设计类的时候，我
们优先考虑通过多重继承来组合多个 MixIn 的功能，而不是设计多层次
的复杂的继承关系"""

# 比如，编写一个多进程模式的 TCP 服务，定义如下：


class ForkingMixin(object):
    pass


class TcpServer(object):
    pass


class MyTCPServer(TcpServer, ForkingMixin):
    pass

"""小结

由于 Python 允许使用多重继承，因此， MixIn 就是一种常见的设计。
只允许单一继承的语言（如 Java）不能使用 MixIn 的设计。"""