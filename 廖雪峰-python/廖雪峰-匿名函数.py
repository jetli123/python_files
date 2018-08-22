# -*- coding: utf-8 -*-
#以 map()函数为例，计算 f(x)=x2 时，除了定义一个 f(x)的函数外，还可以直接传入匿名函数：
print list(map(lambda x: x * x, [1, 2, 3, 4]))

# 匿名函数 lambda 实际上就是:
#def f(x):
#   return x * x
# 关键字 lambda 表示匿名函数，冒号前面的 x 表示函数参数


# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，
# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利
# 用变量来调用该函数：
f = lambda x: x * x
print f(4)
print f.__name__  # 获取函数名
# 同样，也可以把匿名函数作为返回值返回，比如：
def build(x, y):
    return lambda: x * x + y * y

b = build(1, 4)
print b()

# 小结：
# Python 对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。