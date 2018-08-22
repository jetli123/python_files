# -*- coding: utf-8 -*-
import shelve


s = shelve.open('test.dat')
s['x'] = ['a', 'b', 'c']
temp = s['x']    # 必须将临时变量绑定到获得的副本上，并在它修改后重新存储这个副本
temp.append('d')
s['x'] = temp
print s['x']
