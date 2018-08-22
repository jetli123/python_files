# -*- coding: utf-8 -*-
"""class"""


class Fod(object):

    name = 'Michel'  # 类的属性

    def __init__(self, value):  # 实例的属性
        self.a = 1
        self.b = []
        self.value = value

    def __str__(self):
        print("Not input any value!")
        return str(self.a)

    __repr__ = __str__

    def __test(self):
        for i in range(self.value):
            if self.a > 300:
                print(u"OMG 退出")
                break
            else:
                self.b.append(self.a + i)
                self.a += i
        return self.b

    def calc(self):
        print self.__test()

if __name__ == '__main__':
    # 正常调用
    t = Fod(5)
    t.calc()
    # print Fod.name
    print t.name