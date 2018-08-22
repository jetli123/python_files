aa = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(aa):

    print index, '-', name

bb = ['Adam', 'Lisa', 'Bart', 'Paul']
for indexs, names in zip(range(1,5), bb):
    print indexs, '-', names

from math import sqrt
for n in range(70, 0, -1):
    root = sqrt(n)
    print root
    if root == int(root):
        print root
        print n
        break

from math import sqrt
for n in range(80, 4, -1):
    aa = sqrt(n)
    if aa == int(aa):
        print n
        break

