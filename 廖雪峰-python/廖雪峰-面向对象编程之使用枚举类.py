# -*- coding: utf-8 -*-
__author__ = 'JetLi'
"""当我们需要定义常量时，一个办法是用大写变量通过整数来定义，"""
# 例如月份：

# JAN = 1
# FEB = 2
# MAR = 3
# ...
# NOV = 11
# DEC = 12
"""好处是简单，缺点是类型是 int，并且仍然是变量。"""

"""更好的方法是为这样的枚举类型定义一个 class 类型，然后，每个常量
都是 class 的一个唯一实例。 Python 提供了 Enum 类来实现这个功能："""

# from enum from Enum
