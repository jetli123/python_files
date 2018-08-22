# -*- coding: utf-8 -*-
"""
接口的概念和多态有关。在处理多态对象时，只要关心它的接口（或称“协议”）即可，
也就是公开的方法和特性。
"""
# 还可以检查所需方法是否已经存在

class Calculator:

    def cal(self, expression):
        self.value = eval(expression)

class Talker:

    def talk(self):
        print "Hi, my value is", self.value

class TalkingCalculator(Calculator, Talker):
    pass

if __name__ == '__main__':

    tc = TalkingCalculator()
    tc.cal('1+2*3')
    tc.talk()
    # 检查方法是否存在
    print '是否存在特性：', hasattr(tc, 'talk')  # 查看talk 特性（包含一个方法）是否存在。
    print '检查talk方法是否可调用：', hasattr(getattr(tc, 'talk', None), '__call__')
    # getattr 函数允许提供默认值（本例为None）,以便在特性不存在时使用。
    # 与 getattr 相对应的函数是 setattr， 可以用来设置对象的特性；
    setattr(tc, 'name', 'Mr, Gumby')
    print tc.name  # Mr, Gumby
    print '查看对象内多有存储的值：', tc.__dict__  # __dict__ 方法查看对象内所有存储的值。
    # {'name': 'Mr, Gumby', 'value': 7}