# -*- coding: utf-8 -*-
def fib(max):
    n, a, b = 0, 0, 1  # 定义 参数值
    while n < max:
        print b       # 输出结果
        a, b = b, a + b   # 赋值
        n = n + 1      # 循环
    return 'done'

fib(6)


def Tst(CE):
    for i in range(1, 8):
        CE.append(CE[-2] + CE[-1])
    return CE

C = [0, 1]
print Tst(C)