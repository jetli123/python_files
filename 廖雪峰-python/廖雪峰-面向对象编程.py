# -*- coding: utf-8 -*-
"""
面向对象编程——Object Oriented Programming，简称 OOP，是一种程
序设计思想。 OOP 把对象作为程序的基本单元，一个对象包含了数据和
操作数据的函数。

"""

# -*- 解释 -*-
"""，而每个对象
都可以接收其
面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数
的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，
即把大块函数通过切割成小块函数来降低系统的复杂度。
-----
面向对象的程序设计把计算机程序视为一组对象的集合他对象发过来的消息，并处理这些消息，计算机程序的执
行就是一系列消息在各个对象之间传递。
"""


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):  # 定义第一个方法
        print '%s: %s' % (self.name, self.score)

    def get_grade(self):  # 定义第二个方法
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

    def who(self):  # 定义第三个方法
        if self.name == 'Miche':
            print 'He is my brother!'
        else:
            print 'He is Shice! Hello.'


miche = Student('Miche', 94)  # 根据 类 :Student(), 创建实例：miche， Student类中 定义 name和 score 属性，必须有值
shice = Student('Shice', 70)  # 根据 类 :Student(), 创建实例：shice， Student类中 定义 name和 score 属性，必须有值

miche.print_score()
Student.print_score(miche)
shice.print_score()
Student.print_score(shice)

print miche.name

print miche.get_grade()
miche.who()
shice.who()
print shice

