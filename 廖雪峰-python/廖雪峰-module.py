#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" a test module"""

__author__ = 'Michael Liao'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print 'This is a python file for %s ' % args[0]
    elif len(args) == 2:
        print 'Hello, %s !' % args[1]
    elif len(args) == 3:
        print 'The second and third parameters is %s, %s' % (args[1], args[2])
    else:
        print 'Too many arguments!'


test()

'''当我们在命令行运行 hello 模块文件时， Python 解释器把一个特殊变量
__name__置为__main__，而如果在其他地方导入该 hello 模块时， if 判断
将失败，因此，这种 if 测试可以让一个模块通过命令行运行时执行一
些额外的代码，最常见的就是运行测试'''

if __name__ == '__main__':
    print "LxFmodule.py 作为主程序运行！"
    raw_input("Enter any str")
