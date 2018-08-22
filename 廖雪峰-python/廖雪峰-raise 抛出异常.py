# -*- coding: utf-8 -*-
# -*- get x^2 create a function -*-
def power(x, n=2):
    if not isinstance(x, int):
        raise TypeError('Function Operand Error!')
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
