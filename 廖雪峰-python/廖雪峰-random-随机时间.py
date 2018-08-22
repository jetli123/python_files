# -*- coding: utf-8 -*-
# 随机获取 2017-2018 年的任意时间
from random import *
from time import *

__author__ = 'JetLi'


def test1():
    date1 = (2017, 1, 1, 0, 0, 0, -1, -1, -1)
    date2 = (2018, 1, 1, 0, 0, 0, -1, -1, -1)
    time1 = mktime(date1)  # 将日期元组 转换为秒数 1488061787.336491
    time2 = mktime(date2)
    rrr = uniform(time1, time2)
    print asctime(localtime(rrr))


test1()
