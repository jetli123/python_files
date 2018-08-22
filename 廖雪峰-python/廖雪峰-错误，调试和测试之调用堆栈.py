# -*- coding: utf-8 -*-
__author__ = 'JetLi'
# 调用堆栈


def foo(s):
    return 10 / int(s)


def bars(s):
    return foo(s) * 2


def mains():
    bars('0')

mains()

"""如果错误没有被捕获，它就会一直往上抛，最后被 Python 解释器捕获，
打印一个错误信息，然后程序退出。"""

"""
错误信息第 1 行：
Traceback (most recent call last):
告诉我们这是错误的跟踪信息。
第 2~3 行：
File "err.py", line 11, in <module>
main()
调用 main()出错了，在代码文件 err.py 的第 11 行代码，但原因是第 9
行：
File "err.py", line 9, in main
bar('0')
调用 bar('0')出错了，在代码文件 err.py 的第 9 行代码，但原因是第 6
行：
File "err.py", line 6, in bar
return foo(s) * 2
原因是 return foo(s) * 2 这个语句出错了，但这还不是最终原因，继续
往下看：
File "err.py", line 3, in foo
return 10 / int(s)
原因是 return 10 / int(s)这个语句出错了，这是错误产生的源头，因为
下面打印了：
ZeroDivisionError: integer division or modulo by zero
根据错误类型 ZeroDivisionError，我们判断， int(s)本身并没有出错，
但是 int(s)返回 0，在计算 10 / 0 时出错，至此，找到错误源头。
"""
