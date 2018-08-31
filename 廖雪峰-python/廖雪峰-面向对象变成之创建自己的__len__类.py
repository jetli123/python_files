# -*- coding: utf-8 -*-

"""创建自己的__len__ 类"""


class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))
