# -*- coding: utf-8 -*-
# 可以直接作用于 for 循环的数据类型有以下几种：
# 一类是集合数据类型，如 list、 tuple、 dict、 set、 str 等；
# 一类是 generator，包括生成器和带 yield 的 generator function。
# 这些可以直接作用于 for 循环的对象统称为可迭代对象： Iterable。
# 可以使用 isinstance()判断一个对象是否是 Iterable 对象：
from collections import Iterable
print isinstance([], Iterable)
print isinstance({}, Iterable)
print isinstance('abc', Iterable)
print isinstance((x for x in range(10)), Iterable)


# 而生成器不但可以作用于 for 循环，还可以被 next()函数不断调用并返
# 回下一个值，直到最后抛出 StopIteration 错误表示无法继续返回下一个值了
# 可以被 next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 可以使用 isinstance()判断一个对象是否是 Iterator 对象：
from collections import Iterator
print isinstance((x for x in range(10)), Iterator)

# 生成器都是 Iterator 对象，但 list、 dict、 str 虽然是 Iterable，却不是 Iterator。
print isinstance([], Iterator)  # -*- {} []  'abc' : False -*-
# 把 list、 dict、 str 等 Iterable 变成 Iterator 可以使用 iter()函数：
print isinstance(iter([]), Iterator)

# 因为 Python 的 Iterator 对象表示的是一个数据流， Iterator 对象可
# 被 next()函数调用并不断返回下一个数据，直到没有数据时抛出 StopIteration 错误。
# 所以 list、 dict、 str 等数据类型不是 Iterator。
print '-*- NEXT -*- '
for x in [1, 2, 3, 4]:
    pass

it = iter([1, 2, 3, 4])
while True:
    try:
        x = next(it)
        print x
    except StopIteration:
        break