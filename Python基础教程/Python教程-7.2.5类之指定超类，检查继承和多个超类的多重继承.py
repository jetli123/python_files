# -*- coding: utf-8 -*-
""""""
""""""""""""""""""""""""""""""""""""""""""
# -*- 超类

class Filter:

    def init(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):

    def init(self):  # 重写 Filter 超类中的 init 方法
        self.blocked = ['SPAM']

""""""""""""""""""""""""""""""""""""""""""
#########################################################
# -*- 多个超类
__metaclass__ = type


class Calculator:

    def cal(self, expression):
        self.value = eval(expression)

class Talker:

    def talk(self):
        print "Hi, my value is", self.value

# 使用多重继承时，需要注意，如果一个方法从多个超类继承，那么必须要注意一下超类的顺序
# 在 class语句中：先继承的类中的方法会重写后继承类的方法，
# 所以如果 Calculator 类也有个叫做 talk 的方法，那么它就会重写Talker类的 talk 方法（使其不可访问）。
# 如果把他们的顺序掉过来：
# class TalkingCalculator(Talker, Calculator):
    #  pass
# 就会让 Talker 类的 task 方法可用了。

class TalkingCalculator(Calculator, Talker):  # TalkingCalculator 类为多重继承
    pass
#########################################################

if __name__ == '__main__':

    """"""""""""""""""""""""""""""""
    f = Filter()
    f.init()
    print f.filter([1, 2, 3])

    s = SPAMFilter()
    s.init()
    print s.filter(['SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM'])
    # 注意：
    # 1.这里提供新定义的方式重写了 Filter 的init 定义。
    # 2.filter方法的定义是从Filter 类中拿过来（继承）的，所以不用重写它的定义
    """"""""""""""""""""""""""""""""

    ###################################
    a = TalkingCalculator()
    a.cal('1+2*3')
    a.talk()

    # 检查继承
    # 检查一个类是否是另一个的子类，可以使用 issubclass :
    print '检查前一个类是否是子类：', issubclass(TalkingCalculator, Talker)
    # 如果想得到已知类的基类（们），可以直接使用它的特殊性 __bases__：
    print '当前类的基类们是：', TalkingCalculator.__bases__
    print Calculator.__bases__
    print '查看对象内多有存储的值：', a.__dict__   # __dict__ 方法查看对象内所有存储的值。
    # 如果使用 __metaclass__ =type 或从object 继承的方式来定义新式类，那么可以使用
    # type(a) 查看实例所属的类。
    print '查看实例所属的类为：', type(a)
    ###################################