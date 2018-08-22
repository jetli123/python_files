# -*- coding: utf-8 -*-
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# -*- 调用函数 my_abs ，x 为负数-*-
print my_abs(-109)
# -*- 测试 x 为字符串，输出 TypeError -*-

def enroll(name, gender, age=6, city='Beijing'):
    print "name:", name
    print "gender:", gender
    print "age:", age
    print "city:", city

enroll('LIli', 'F')
enroll('Cati', 'A', 9)
enroll('Natasha', 'N', city='Nanjing')

# -*- 函数默认参数要指向不变对象 list [] 是可变对象-*-
def add_end(L=[]):
    L.append('End')
    return L

print add_end([1, 2])
print add_end()
print add_end()

# -*- 修改为 L=None -*-
def add_ends(L=None):
    if L is None:
        L = []
    L.append('End')
    return L

print add_ends()
print add_ends()