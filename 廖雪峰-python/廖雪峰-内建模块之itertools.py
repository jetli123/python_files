# -*- coding: utf-8 -*-
"""Python 的内建模块 itertools 提供了非常有用的用于操作迭代对象的函
数。"""

"""无限迭代器 count"""
import itertools

natuals = itertools.count(-3)
for n in natuals:
    if n > 14:
        break
    print n
# 因为 count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，
# 根本停不下来，只能按 Ctrl+C 退出。

"""cycle()"""
# cycle()会把传入的一个序列无限重复下去

cs = itertools.cycle('ABC')
count = 0
for c in cs:
    if count > 5:
        break
    else:
        print c
    count += 1

# 根本停不下来，只能按 Ctrl+C 退出


"""repeat()"""
# 负责把一个元素无限重复下去，不过如果提供第二个参数就可
# 以限定重复次数：

ns = itertools.repeat('LOVE', 2)
for n in ns:
    print n

"""takewhile()"""
# 无限序列虽然可以无限迭代下去，但是通常我们会通过 takewhile()等函
# 数根据条件判断来截取出一个有限的序列：

ab = itertools.count(1)
ac = itertools.takewhile(lambda x: x <= 10, ab)
print list(ac)

"""chain()"""
#  chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for ob in itertools.chain('ABD', 'OMU'):
    print ob

"""groupby()"""
# groupby()把迭代器中相邻的重复元素挑出来放在一起：

for key, group in itertools.groupby('AAABBBCCAAAA'):
    print key, list(group)

# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的
# 值相等，这两个元素就被认为是在一组的，而函数返回值作为组的 key。
# 如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的 key：

for keys, groups in itertools.groupby('AaaBbCCcAaaA', lambda c: c.upper()):
    print keys, list(groups)