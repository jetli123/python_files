# -*- coding: utf-8 -*-
__author__ = 'JetLi'
"""由于 Python 是动态语言，根据类创建的实例可以任意绑定属性。
给实例绑定属性的方法是通过实例变量，或者通过 self 变量："""

class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Jet')
print s.name
# Jet

"""但是，如果 Student 类本身需要绑定一个属性呢？可以直接在 class 中定
义属性，这种属性是类属性，归 Student 类所有："""
class Stu(object):
    name = 'Stu'

b = Stu()  # 创建实例 s
print b.name   # 打印 name 属性，因为实例并没有 name 属性，所以会继续查找 class 的 name 属性
#  Stu
b.name = 'Michael'  # 给实例绑定 name 属性
print b.name  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的 name 属性
# Michael
print Stu.name  # 但是类属性并未消失，用 Student.name 仍然可以访问
# Stu

del b.name  # 如果删除实例的 name 属性
print b.name  # 再次调用 s.name，由于实例的 name 属性没有找到，类的 name 属性就显示出来了
# Stu

"""从上面的例子可以看出，在编写程序的时候，千万不要把实例属性和类
属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是
当你删除实例属性后，再使用相同的名称，访问到的将是类属性"""
