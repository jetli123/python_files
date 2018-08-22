# -*- coding: utf-8 -*-
# -*- 函数和 generator 仅一步之遥。要把 fib 函数变成 generator，只需要把 print(b)改为 yield b 就可以了 -*-
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

f = fib(8)
#print next(f)
#print next(f)
#print next(f)
#print next(f)
# print next(f)
# print next(f)

# -*- 通过 for 循环 打印 结果 -*-
for i in f:
    print i
# -*- 定义一个 generator，依次返回数字 1，3，5 -*-
def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5

o = odd()
print next(o)
print next(o)
print next(o)
