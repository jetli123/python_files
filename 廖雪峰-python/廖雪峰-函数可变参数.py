# -*- coding: utf-8 -*-
# -*- 调用的时候，需要先组装出一个 list 或 tuple -*-
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc([2, 3])  # -*- 参数为 list -*-
print calc((3, 2)) # -*- 参数为 tuple -*-

# -*- 如果调用函数的方式简化成 calc(1, 2, 3) -*-
# -*- 那么改成可变参数 *numbers -*-
# -*- 可变参数允许你传入 0 个或任意个参数，这些可变参数在函数调用时自 -*-
# -*- 动组装为一个 tuple。 -*-

def cala(*nums):
    sums = 0
    for x in nums:
        sums = sums + x * x
    return sums
print cala(1, 2, 3)

# -*- 如果已经有一个 list or tuple 调用可变参数 -*-
numss = [1, 2, 3, 4]  # -*- list -*-
print cala(*numss)
nba = (2, 4, 6)       # -*- tuple -*-
print cala(*nba)

