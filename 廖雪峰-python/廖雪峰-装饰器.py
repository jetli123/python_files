# -*- coding: utf-8 -*-
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。


def now():
    print('时间：2017-11-04')

f = now  # 函数 now 作为对象 赋值给 变量 f
f()

# 函数对象有一个__name__属性，可以拿到函数的名字：
print 'now的__name__属性为：', now.__name__
print '函数f()的name属性为：', f.__name__

# 现在，假设我们要增强 now()函数的功能，比如，在函数调用前后自动
# 打印日志，但又不希望修改 now()函数的定义，这种在代码运行期间动
# 态增加功能的方式，称之为“装饰器”（Decorator）。


def log(func):
    def wrapper(*args, **kw):
        if __name__ == '__main__':
            if __name__ == '__main__':
                print 'call %s():' % func.__name__
            return func(*args, **kw)
    return wrapper


@log
def now():
    print '2017-11-22'
now()

