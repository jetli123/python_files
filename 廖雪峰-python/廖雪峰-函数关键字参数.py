# -*- coding: utf-8 -*-
# -*- 关键字参数允许你传入 0 个或任意个含参数名的参数，-*-
# -*- 这些关键字参数在函数内部自动组装为一个 dict。 -*-

def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw

person('Admin', 22)  # -*- name: Admin age: 22 other: {} -*-

# -*- 传入任意关键字参数 -*-
person('Bob', 30, city='Beijing') # -*- result: name: Bob age: 30 other: {'city': 'Beijing'} -*-
person('Bob', 30, genter='M', city='Beijing')
# -*- result: name: Bob age: 30 other: {'genter': 'M', 'city': 'Beijing'} -*-

# -*- 组装一个 dict ，将dict 转换为 关键字参数传进去 -*-
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person('Jack', 24, city=extra['city'], job=extra['job'])   # -*- 此方法比较复杂 -*-

# -*- 简化方法调用 -*-
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)