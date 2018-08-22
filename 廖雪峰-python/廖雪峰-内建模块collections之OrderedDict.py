# -*- coding: utf-8 -*-
from collections import OrderedDict

# 使用 dict 时，Key 是无序的。在对 dict 做迭代时，我们无法确定 Key的顺序。
# 如果要保持 Key 的顺序，可以用 OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print d
# {'a': 1, 'c': 3, 'b': 2}
de = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print de
# OrderedDict([('a', 1), ('b', 2), ('c', 3)])
'''注意， OrderedDict 的 Key 会按照插入的顺序排列，不是 Key 本身排序'''
cd = OrderedDict()
cd['z'] = 1
cd['y'] = 2
cd['x'] = 3
print list(cd.keys())  # # 按照插入的 Key 的顺序返回
#  ['z', 'y', 'x']

# OrderedDict 可以实现一个 FIFO（先进先出）的 dict，当容量超出限制
# 时，先删除最早添加的 Key：


class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self.capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self.capacity:
            last = self.popitem(last=False)
            print 'remove: ', last
        if containsKey:
            del self[key]
            print 'set: ', (key, value)
        OrderedDict.__setitem__(self, key, value)

cd['a'] = 4
print cd
