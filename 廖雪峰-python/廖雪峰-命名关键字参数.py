# -*- coding: utf-8 -*-
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print 'name:', name, 'age:', age, 'other:', kw

# -*- 但是调用者仍可以传入不受限制的关键字参数 -*-
person('Jack', 22, city='Beijing', addr='Chaoyang', zipcode=123456)

# -*- 使用命名关键字参数 -*-
#def person(name, age, *, city, job):    # Python 2.7 不支持，等待升级到Python3
#    print(name, age, city, job)


# -*-m参数组合 使用 -*-
def f1(name, old, size=0, *args, **kw):
    print 'name =', name, 'old =', old, 'size =', size, 'args =', args, 'kw =', kw

dd = {'ages': 22, 'address': 'Beijing'}
cc = (1, 2, 3, 4)
f1('Jack', 23, 330, *cc, **dd)
f1(*cc, **dd)