# -*- coding: utf-8 -*-
"""
    collections 是 Python 内建的一个集合模块，提供了许多有用的集合类。
"""
from collections import namedtuple, Counter
from collections import deque, defaultdict
# from collections import OrderedDict


print 'START: namedtuple'
"""namedtuple"""
# 我们知道 tuple 可以表示不变集合，例如，一个点的二维坐标就可以表
# namedtuple 是一个函数，它用来创建一个自定义的 tuple 对象，并且规
# 定了 tuple 元素的个数，并以用可属性而不是索引来引用 tuple 的某个元素。
# 这样一来，我们用 namedtuple 可以很方便地定义一种数据类型，它具备
# tuple 的不变性，又可以根据属性来引用，使用十分方便
point = namedtuple('Point', ['x', 'y'])
p = point(1, 2)
print p.x, p.y
'''这样一来，我们用 namedtuple 可以很方便地定义一种数据类型，它具备
tuple 的不变性，又可以根据属性来引用，使用十分方便。'''
print isinstance(p, point)  # True
print isinstance(p, tuple)  # True
'''类似的，如果要用坐标和半径表示一个圆，也可以用 namedtuple 定义：'''
# namedtuple('名称', [属性 list]):
# circle = namedtuple('Circle', ['x', 'y', 'r'])


print 'START: deque'
"""deque 双向列表"""
# 使用 list 存储数据时，按索引访问元素很快，但是插入和删除元素就很
# 慢了，因为 list 是线性存储，数据量大的时候，插入和删除效率很低。
# deque 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
q = deque(['a', 'b', 'c'])
q.append('x')  # 默认往最后添加元素
q.appendleft('y')  # 往头部添加元素
print q
# deque(['y', 'a', 'b', 'c', 'x'])
# deque 除了实现 list 的 append()和 pop()外，还支持 appendleft()和
# popleft()，这样就可以非常高效地往头部添加或删除元素。
print q.pop()  # 默认删除尾部元素
print q
print q.popleft()  # 默认删除头部元素
print q


print 'START: defaultdict'
"""defaultdict"""
# 使用 dict 时，如果引用的 Key 不存在，就会抛出 KeyError。如果希望
# key 不存在时，返回一个默认值，就可以用 defaultdict：
dd = defaultdict(lambda: 'N/A')   # 定义函数，设置默认值 N/A
dd['key1'] = 'abc'
print dd['key1']
print dd['key2']  # 调用函数返回默认值 'N/A'
# 注意默认值是调用函数返回的，而函数在创建 defaultdict 对象时传入。
# 除了在 Key 不存在时返回默认值，defaultdict 的其他行为跟 dict 是完全一样的。


print 'START: Counter'
"""Counter"""
# 一个简单的计数器，
# 例如，统计字符出现的个数：
c = Counter()
for ch in 'programming':
    c[ch] += 1
print c
# Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
