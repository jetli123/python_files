# -*- coding: utf-8 -*-
# 要求用户投掷的骰子数以及每个骰子具有的面数

from random import randrange

__author__ = 'JetLi'

num = input('How many dice? ')
sides = input('How many sides per die? ')
som = 0
for i in range(num):
    som += randrange(sides) + 1   # randrange(sides) + 1 == randrange(1, 7)  随机去1-7 的 6个数，不包括7
print 'The result is', som
