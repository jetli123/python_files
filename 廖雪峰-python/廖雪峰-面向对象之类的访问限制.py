# -*- coding: utf-8 -*-
"""在 Class 内部，可以有属性和方法，而外部代码可以通过直接调用实例
变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。"""


class Student(object):  # 目前 外部代码还是可以自由地修改一个实例的 name、 score 属性
    def __init__(self, name, score):
        self.name = name  #
        self.score = score  #

    def print_score(self):
        print '%s: %s' % (self.name, self.score)


# 例如：
bart = Student('Bart Simpson', 98)
print bart.score  # 98
# 修改 score 变量
bart.score = 10
print bart.score  # 10

"""如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线
__，在 Python 中，实例的变量名如果以__开头，就变成了一个私有变量
（private），只有内部可以访问，外部不能访问，"""


class Stud(object):  # 目前 外部代码还是可以自由地修改一个实例的 name、 score 属性
    def __init__(self, names, scores):
        self.__names = names  # 加 _ _ 变为私有变量
        self.__scores = scores  # 加 _ _ 变为私有变量

    def print_scores(self):
        print '%s: %s' % (self.__names, self.__scores)

    def get_names(self):  # 通过 此方法 访问names 变量
        return self.__names

    def get_scores(self):  # 通过 此方法 访问 scores 变量
        return self.__scores

    def set_score(self, scores):  # 通过 set_score 方法 修改 scores 变量
        if 0 <= scores <= 100:
            self.__scores = scores
        else:
            raise ValueError('Bad scores')


"""但是如果外部代码要获取 name 和 score 怎么办？可以给 Student 类增加
get_name 和 get_score 这样的方法："""

Jet = Stud('OBD', 20)

print Jet.get_names()  # 通过 get_names方法 访问names 变量
print Jet.get_scores()  # 通过 get_scores方法 访问 scores 变量

Jet.set_score(80)  # 通过 set_score 方法 修改 scores 变量
print Jet.get_scores()  # 80

"""在 Python 中，变量名类似__xxx__的，也就是以双下划
线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访
问的，不是 private 变量，所以，不能用__name__、 __score__这样的变量
名。"""

"""不能直接访问__name 是因为 Python 解释器对外把__name 变量改成了
_Student__name，所以，仍然可以通过_Student__name 来访问__name 变量："""

print Jet._Stud__names
