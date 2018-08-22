# -*- coding: utf-8 -*-
__author__ = 'JetLi'
"""因为错误是 class，捕获一个错误就是捕获到该 class 的一个实例。因此，
错误并不是凭空产生的，而是有意创建并抛出的。 Python 的内置函数会
抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

如果要抛出错误，首先根据需要，可以定义一个错误的 class，选择好继
承关系，然后，用 raise 语句抛出一个错误的实例"""

"""
class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

print foo('0') """
import logging


def eoo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        eoo('0')
    except ValueError:
        print('ValueError!')
        logging.exception(ValueError)
        raise


bar()


def abc():
    try:
        a = 10 / 0
    except ZeroDivisionError:
        raise ValueError('input error!')
    finally:
        print 'finally...'
        logging.exception(ZeroDivisionError)
    print 'END'

abc()
