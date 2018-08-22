def getprice(objects):
    ##if ('aa', 22, 'bb', 33)
    if isinstance(objects, tuple):
        print objects
        return objects[1]
    ##if {'aa': 2, 'cc': 3 }
    elif isinstance(objects, dict):
        print objects
        return int(objects['price'])
    else:
        return len(objects)
aa = {'SPAM': 22, 'price': 11}
bb = 'banana', '44', 'apple', '43'
print getprice(bb)

print [1, 2, 'a', 'a', 'c'].count('c')
print 'abaac'.count('a')

def add(x, y):
    return x+y
print add(1, 2)
print add('Jet', 'Li')
print add('(1, 2)', '[3, 4]')