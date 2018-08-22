# -*- coding: utf-8 -*-
# -*- 一边循环一边计算的机制，称为生成器: generator -*-
print [pow(x, 2) for x in range(1, 10)]  # -*- 结果是 list -*-
#g = (y * y for y in range(1, 10))  # -*- 结果是 generator -*-
#print next(g)  # 打印 generator 通过 next() 函数
#print next(g)
#print next(g)
# -*- 正确方式通过 for 循环 迭代 generator -*-
#for n in g:
#    print n

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

g = fib(6)

while True:
    try:
        x = next(g)
        print 'g:', x
    except StopIteration as e:
        print 'Generator return  value:', e.message
        break

