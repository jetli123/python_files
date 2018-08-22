# -*- coding: utf-8 -*-
__author__ = 'Jet li'

"""封装的另一个好处是可以给 Student 类增加新的方法，"""

"""既然 Student 实例本身就拥有这些数据，要访问这些数据，就没
有必要从外面的函数去访问，可以直接在 Student 类的内部定义访问数
据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和
Student 类本身是关联起来的，我们称之为类的方法："""


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

"""要定义一个方法，除了第一个参数是 self 外，其他和普通函数一样。要
调用一个方法，只需要在实例变量上直接调用，除了 self 不用传递，其
他参数正常传入："""
bart = Student('Bart Simpson', 59)  # 根据类 Student 创建实例：bart
lisa = Student('Lisa Simpson', 87)  # 根据类 Student 创建实例：lisa
bart.print_score()  # 调用类 内部的 方法
print lisa.name  # 外部可以直接调用实例的 name 变量  注：内部叫类的属性，外部调用叫实例的变量

""" 这样一来，我们从外部看 Student 类，就只需要知道，创建实例需要给
出 name 和 score，而如何打印，都是在 Student 类的内部定义的，这些
数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细
节。 """

"""封装的另一个好处是可以给 Student 类增加新的方法，比如 get_grade："""
"""同样的， get_grade 方法可以直接在实例变量上调用，不需要知道内部实
现细节："""
print lisa.get_grade()
# 在创建一个新实例
omu = Student('Ahub', 101)
# 调用 类中的 封装的 get_grade 函数
print omu.get_grade()

""" 小结：
1.类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
2.方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
3.通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。"""

"""和静态语言不同， Python 允许对实例变量绑定任何数据，也就是说，对
于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名
称都可能不同："""
omu.sce = 1
print omu.sce
#print lisa.sce
