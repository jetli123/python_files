# -*- coding: utf-8 -*-
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# -*- 注：原来返回值是一个 tuple！ 但是，在语法上，返回一个 tuple 可以省略括 -*-
# -*- 号，而多个变量可以同时接收一个 tuple，按位置赋给对应的值，所以，-*-
# -*- Python 的函数返回多值其实就是返回一个 tuple，但写起来更方便。 -*-
r = move(100, 200, 4, math.pi / 6)
print r  # -*- (103.46410161513775, 198.0) -*-
