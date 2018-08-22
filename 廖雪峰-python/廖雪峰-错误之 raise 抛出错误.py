# -*- coding: utf-8 -*-
"""因为错误是 class，捕获一个错误就是捕获到该 class 的一个实例。因此，
错误并不是凭空产生的，而是有意创建并抛出的。 Python 的内置函数会
抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
如果要抛出错误，首先根据需要，可以定义一个错误的 class，选择好继
承关系，然后，用 raise 语句抛出一个错误的实例："""
# 例子1：

class FooError(Exception):
    pass


def foo1(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo1(10)

# 例子2：
'''捕获错误目的只是记
录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错
误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一
个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也
处理不了，就一直往上抛，最终会抛给 CEO 去处理。 '''

def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError:
        print('ValueError!')
        raise

bar()