# -*- coding: utf-8 -*-
# 发牌，回车为自己发一张牌，并不能重复
__author__ = 'JetLi'

from random import shuffle
from pprint import pprint

values = range(2, 11) + 'J Q K A'.split()
suits = 'Ho Fa he Ha'.split()
deck = ['%s %s' % (s, v) for s in suits for v in values]
shuffle(deck)

pprint(deck[:12])
# while deck:
#     raw_input(deck.pop())    # list pop() 方法 移除列表中的一个元素，并返回该元素的值
