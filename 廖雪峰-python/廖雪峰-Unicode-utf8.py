# -*- coding: utf-8 -*-
# -*-  你好 -*-
print 'hello, %s' % 'world'
print 'hello %s, you have $%d' % ('Micheal', 100000)
hight = 1.75
weight = 80.5
bmi = weight / pow(hight, 2)
if bmi < 18.5:
    print('He is empty!')
elif 18.5 <= bmi < 25:
    print('He is OK!')
elif 25 <= bmi < 28:
    print('He is weight!')
elif 28 <= bmi < 32:
    print('He is more than weighter!')
else:
    print('He is most weightest!')

L = ['Bart', 'Lisa', 'Adam']
for x in range(3):
    print 'Hello, %s!' % L[x]

