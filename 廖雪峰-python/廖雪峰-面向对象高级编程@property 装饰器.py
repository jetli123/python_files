# -*- coding: utf-8 -*-
"""在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但
是，没办法检查参数，导致可以把成绩随便改："""

'''为了限制 score 的范围，可以通过一个 set_score()方
法来设置成绩，再通过一个 get_score()来获取成绩，这样，在 set_score()
方法里，就可以检查参数：'''


class Student(object):

    def __init__(self):
        self.__score = None

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer!')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 and 100 !')
        self.__score = score

# 现在，对任意的 Student 实例进行操作，就不能随心所欲地设置 score了
s = Student()
s.set_score(80)
print s.get_score()
# 80

"""这种使用 get/set 方法来封装对一个属性的访问在许多面向对象编程的语言中都很常见。
但是写 s.get_score() 和 s.set_score() 没有直接写 s.score 来得直接。
有没有两全其美的方法？----有。

因为Python支持高阶函数，可以用装饰器函数把 get/set 方法“装饰”成属性调用："""


class Students(object):

    def __init__(self):
        self.__scores = None

    @property    # Python 内置的@property 装饰器就是负责把一个方法变成属性调用的：
    def scores(self):    # 第一个scores(self)是get方法  用@property装饰
        return self.__scores

    @scores.setter  # @scores.setter是前一个@property 装饰后的副产品
    def scores(self, value):  # 第二个scores(self, score)是set方法，用@scores.setter 装饰

        if not isinstance(value, int):
            raise ValueError('scores must by integer!')

        if value < 0 or value > 100:
            raise ValueError('scores must between 0 ~ 100!')
        self.__scores = value

"""@property 的实现比较复杂，我们先考察如何使用。把一个 getter 方法变
成属性，只需要加上@property 就可以了，此时， @property 本身又创建
了另一个装饰器@score.setter，负责把一个 setter 方法变成属性赋值，
于是，我们就拥有一个可控的属性操作："""

d = Student()
d.scores = 60  # OK，实际转化为 s.set_score(60)
print d.scores  # OK，实际转化为 s.get_score()
# 60

"""注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该
属性很可能不是直接暴露的，而是通过 getter 和 setter 方法来实现的。"""

# 还可以定义只读属性，只定义 getter 方法，不定义 setter 方法就是一个只读属性：


# noinspection PyPropertyDefinition
class Stu(object):

    def __init__(self):
        self.__birth = None

    @property
    def birth(self):  # birth 读属性
        return self.__birth

    @birth.setter
    def birth(self, value):  # birth 写属性
        self.__birth = value

    @property
    def age(self):  # age 只读属性
        return 2016 - self.__birth + 2

x = Stu()
x.birth = 1
print x.birth
print x.age