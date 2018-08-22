# -*- coding: utf-8 -*-
"""
  有的错误是程序编写有问题造成的，比如本来应该输出整数结果输出了
字符串，这种错误我们通常称之为 bug，

 bug 是必须修复的。

 我们也需要跟踪程序的执行，查看变量的值是否正确，这个过程
称为调试。 Python 的 pdb 可以让我们以单步方式执行代码。"""

# 错误处理

# 15145069437

"""所以高级语言通常都内置了一套 try...except...finally...的错误处理
机制， Python 也不例外。"""
print '例子1:'
try:
    print 'try...'
    r = 10 / 2
    print 'result:', r
except ZeroDivisionError as e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'

print '例子2:'
try:
    print 'try...'
    d = 2 / 0
    print 'result:', d
except ZeroDivisionError as a:
    print 'except:', a
finally:
    print 'finally...'
print 'END'

print '例子3:'
try:
    print 'try...'
    r = 10 / 2
    print 'result:', r
except ValueError as e:
    print 'ValueError:', e
except ZeroDivisionError as e:
    print 'ZeroDivisionError:', e
else:
    print 'No Error!'
finally:
    print 'finally...'
print 'END'

"""Python 的错误其实也是 class，所有的错误类型都继承自 BaseException，
所以在使用 except 时需要注意的是，它不但捕获该类型的错误，还把其
子类也“一网打尽”。"""


"""Python 所有的错误都是从 BaseException 类派生的"""

print '例子4:'


def foo():
    AB = -1
    if AB == -1:
        return -1
    # do something
    return AB
try:
    print 'try...'
    foo()
except UnicodeError as e:
    print 'UnicodeError:', e
except ValueError as e:
    print 'ValueError:', e
else:
    print 'No Error!'
finally:
    print 'finally...'
print 'END'


"""第二个 except 永远也捕获不到 UnicodeError，因为 UnicodeError 是
ValueError 的子类，如果有，也被第一个 except 给捕获了。"""


# 使用 try...except 捕获错误还有一个巨大的好处，就是可以跨越多层调用
print '例子5:'


def fooo(s):
    return 10 / int(s)


def bar(s):
    return fooo(s) * 2


def main():
    try:
        print 'try...'
        bar('0')
    except Exception as e:
        print 'Exception:', e
    finally:
        print 'finally...'
    print 'END'

print main()
