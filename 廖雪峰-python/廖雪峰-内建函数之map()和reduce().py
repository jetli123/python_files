# -*- coding: utf-8 -*-
"""
    map()函数接收两个参数，一个是函数，一个是 Iterable，
map 将传入的函数依次作用到序列的每个元素，并把结果作为新的
Iterator 返回。 """
import logging
logging.basicConfig(level=logging.INFO)

"""map()"""
# 比如我们有一个函数 f(x)=x^2
# ，要把这个函数作用在一个 list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，
# 就可以用 map()实现如下


def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5])  # 结果 r 是一个Iterator, Iterator 是惰性序列
print list(r)  # 因此通过 list()函数让它把整个序列都计算出来并返回一个 list。

# 还可以计算任意复杂的函数，比如，把这个list 所有数字转为字符串：
print list(map(str, [1, 2, 3, 4, 5]))
# ['1', '2', '3', '4', '5']


"""reduce()"""
# reduce 把一个函数作用在一个序列[x1, x2, x3, ...]
# 上，这个函数必须接收两个参数，reduce 把结果继续和序列的下一个元
# 素做累积计算，其效果就是：
"""reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)"""
from functools import reduce


def add(x, y):
    return x + y

print reduce(add, [1, 3, 5, 7, 9])
# 25

# 如果要把序列[1, 3, 5, 7, 9]变换成整数 13579，reduce 就可以派上用场：


def fn(x, y):
    return x * 10 + y

print reduce(fn, [1, 3, 5, 7, 9])
# 13579

"""如果考虑到字符串 str 也是一个序列，
对上面的例子稍加改动，配合 map()，我们就可以写出把 str 转换为 int
的函数："""


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print map(char2num, '13579')
print reduce(fn, map(char2num, '13579'))

"""整理成一个 str2int 的函数就是："""


def str2int(d):

    def fm(x, y):
        return x * 10 + y

    def char2number(ac):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[ac]

    return reduce(fm, map(char2number, d))

logging.info(str2int('97531'))

"""还可以用 lambda 函数进一步简化成："""


def str2ints(a):
    return reduce(lambda x, y: x * 10 + y, map(char2num, a))

logging.info(str2ints('13071180239'))

"""练习：1"""
# 利用 map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam',
# 'Lisa', 'Bart']：


def normalize(name):
    return name[0].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'Bart']
print list(map(normalize, L1))

"""练习：2"""
# Python 提供的 sum()函数可以接受一个 list 并求和，请编写一个 prod()
# 函数，可以接受一个 list 并利用 reduce()求积：


def prod(l2):

    if isinstance(l2, list):
        def com(x, y):
            return x * y
        return reduce(com, l2)
    else:
        logging.info(ValueError('invalid value: %s', l2))

print '3 * 5 * 7 * 9 =', prod([3, 5, 7, 9])

"""例子3："""
# 利用 map 和 reduce 编写一个 str2float 函数，把字符串'123.456'转换成
# 浮点数 123.456：


def str2float(h):

    def list2float(x, y):
        return x + y

    def str2list(k):
        return str(k)

    return reduce(list2float, map(str2list, h))

print 'str2float(\'123.456\') =', str2float('123.456')
