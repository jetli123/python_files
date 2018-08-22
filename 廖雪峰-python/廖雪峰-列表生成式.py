# -*- coding: utf-8 -*-
L = []
for x in range(1, 10):
    L.append(x*x)
print L

# -*- 使用函数表示 -*-
def Tes(A):
    for x in range(1, 7):
        A.append(x*x)
    print A
B = []
Tes(B)
# -*- 练习使用列表生成器 -*-
print [x * x for x in range(1, 5)]

# -*- 使用两层循环 -*-
print [m + n for m in 'ABC' for n in 'XYZ']

# -*- 列出当前目录所有文件和目录 -*-
import os
print [b for b in os.listdir('E:/')]

# -*- for 循环可同时使用多个变量 -*-
d = {'x': '1', 'y': '4', 'z': '2'}
print [k + '=' + v for k, v in d.items()]

# -*- 将所有字符串变成小写 -*-
f = ['REDHAT', 'HP', 'Oracle', 'Cisco', 'IBM']
print [s.lower() for s in f]

# -*- 例子 -*-
# -*- 期待输出: ['hello', 'world', 'apple'] -*-
# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x for x in L1 if isinstance(x, str) ] # -*- isinstance() 判断 x 是否是 str 类型 -*-
print(L2)