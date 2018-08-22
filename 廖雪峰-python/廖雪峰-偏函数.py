# -*- coding: utf-8 -*-
# int()函数可以把字符串转换为整数，当仅传入字符串时， int()函数默认按十进制转换
print int('1234')
#但 int()函数还提供额外的 base 参数，默认值为 10。如果传入 base 参数，就可以做 N 进制的转换
print int('01011111', base=2)

#假设要转换大量的二进制字符串，每次都传入 int(x, base=2)非常麻烦，
#于是，我们想到，可以定义一个 int2()的函数，默认把 base=2 传进去
def int2(x, base=2):
    return int(x, base)

print int2('11000000')

# functools.partial 就是帮助我们创建一个偏函数的，不需要我们自己定
# 义 int2()，可以直接使用下面的代码创建一个新的函数 int2
import functools
int3 = functools.partial(int, base=2)
print int3('11100000')

#也可以在函数调用时传入其他值
print int3('11100000', base=10)