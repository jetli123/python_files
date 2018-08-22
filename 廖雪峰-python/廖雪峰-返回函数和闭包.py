# -*- coding: utf-8 -*-
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

d = (1, 2, 3, 5)
print calc_sum(*d)

# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，返回求和的函数
def lazy_sum(*ab):
    def sum():
        xx = 0
        for n in ab:
            xx = xx + n
        return xx
    return sum

f = lazy_sum(1, 2, 4, 5)
print f()

# 在这个例子中，我们在函数 lazy_sum 中又定义了函数 sum，并且，内部
# 函数 sum 可以引用外部函数 lazy_sum 的参数和局部变量，当 lazy_sum 返
# 回函数 sum 时，相关参数和变量都保存在返回的函数中，这种称为“闭包
# （Closure） ”的程序结构拥有极大的威力。

# -*- 闭包 -*-
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1()
print f2()
print f3()

# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量， 或者后
# 续会发生变化的变量。