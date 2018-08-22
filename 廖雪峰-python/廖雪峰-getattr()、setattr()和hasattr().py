# -*- coding: utf-8 -*-
"""仅仅把属性和方法列出来是不够的，配合 getattr()、setattr()以及
hasattr()，我们可以直接操作一个对象的状态："""


class MyDog(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def power(self):
        print self.x * self.y


obj = MyDog(9, 2)
obj.power()

"""紧接着，可以测试该对象的属性"""
print hasattr(obj, 'y')  # 有属性 'y' 吗？
setattr(obj, 'z', 10)  # 设置一个属性 'z'
print hasattr(obj, 'z')  # 有属性 'z' 吗？
print getattr(obj, 'y')  # 获取属性 'y'
#  print obj.z  # 获取属性 'z'

"""可以传入一个 default 参数，如果属性不存在，就返回默认值："""
print getattr(obj, 'a', 404)  # 获取属性 'a'，如果不存在，返回默认值 404

"""也可以获得对象的方法："""
print hasattr(obj, 'power')  # 有属性 'power' 吗？
print getattr(obj, 'power')  # 获取属性 'power'

# 小结：

"""通过内置的一系列函数，我们可以对任意一个 Python 对象进行剖析，
拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
sum = obj.x + obj.y
就不要写：
sum = getattr(obj, 'x') + getattr(obj, 'y')"""

su = obj.x + obj.y
print 'SU:', su

"""如果想用hasattr:"""


def ReadImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None

"""假设我们希望从文件流 fp 中读取图像，我们首先要判断该 fp 对象是否
存在 read 方法，如果存在，则该对象是一个流，如果不存在，则无法读
取。hasattr()就派上了用场。"""
