# -*- coding: utf-8 -*-
# 新建文本文件，每行代表一种运势，通过 FileInput 模块将“运势”都存入列表，在随机抽取
__author__ = 'JetLi'

import fileinput
import random
import time


def fil():
    color = list(fileinput.input('D:\Python27\python file\colors.txt'))
    YS = list(fileinput.input('D:\Python27\python file\yunshi.txt'))
    xz = list(fileinput.input('D:\Python27\python file\XZ.txt'))
    print '今日运势: %s ' % random.choice(YS)  # choice 从给定的文本序列中，随机选择元素
    # print '拥有 %d 颗星' % random.randrange(1, 5)
    print '幸运颜色: %s' % random.choice(color)
    print '幸运数字: %d' % random.randrange(1, 11)
    print '速配星座: %s' % random.choice(xz)
    # print '健康指数: %i%%' % random.randrange(75, 100)
    a = random.randrange(75, 101)
    b = random.randrange(1, 6)          # randrange 从给定的 1-6 范围内，选择 1，2，3，4，5, 6的随机整数
    if 75 <= a < 80 and b <= 3:
        print '健康指数: %i%%' % a
        print '拥有 %d 颗星' % b
        print '短评：情绪波动较大，对现状有许多不满。'
    elif 80 <= a <= 100 and b == 1:
        print '健康指数: %i%%' % a
        print '拥有 %d 颗星' % b
        print '短评：你的未来很美好，但是现实很残酷。'
    elif 85 < a <= 100 and b == 2:
        print '健康指数: %i%%' % a
        print '拥有 %d 颗星' % b
        print '短评：没人任何人动摇你，但你自己很寡断。'
    elif 90 <= a <= 100 and b == 3:
        print '健康指数: %i%%' % a
        print '拥有 %d 颗星' % b
        print '短评：你是一个正直的人，但是别人可能会影响你。'
    elif 75 <= a <= 85 and b == 4:
        print '健康指数: %i%%' % a
        print '拥有 %d 颗星' % b
        print '短评：换上新衣服，收货会很多。'
    elif 75 <= a <= 85 and b == 5:
        print '健康指数: %i%%' % a
        print '拥有 %d 颗星' % b
        print '短评：注意言行，收货非常多。'
    elif 80 <= a <= 85 and 1 < b <= 3:
        print '健康指数: %i%%' % a
        print '拥有 %d 颗星' % b
        print '短评：与长辈相处也要讲究方式。'
    elif 85 < a < 90 and b >= 3:
        print '健康指数: %i%%' % a
        print '拥有 %d 颗星' % b
        print '短评：一切进展顺利。'
    elif 90 <= a < 95 and b >= 4:
        print '健康指数: %i%%' % a
        print '拥有 %d 颗星' % b
        print '短评：求财欲望强烈，进财机会颇多。'
    elif 95 <= a < 97 and b >= 4:
        print '健康指数: %i%%' % a
        print '拥有 %d 颗星' % b
        print '短评：家是你的避风港湾。'
    elif 97 <= a <= 100 and b >= 4:
        print '健康指数: %i%%' % a
        print '拥有 %d 颗星' % b
        print '短评：爱情发挥了奇特的魔力。'
    elif 99 <= a <= 100 and b == 5:
        print '健康指数: %i%%' % a
        print '拥有 %d 颗星' % b
        print '短评：无与匹敌的你，一切尽在掌握中。'
    else:
        print '健康指数: %i%%' % a
        print '拥有 %d 颗星' % b
        print '短评：非常糟糕。'
    time.sleep(3)

fil()
