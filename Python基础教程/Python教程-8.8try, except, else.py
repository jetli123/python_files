# -*- coding: utf-8 -*-
"""有些情况中，没有坏事发生时执行一段代码是很有用的；例如循环"""

while True:
    try:
        x = input('Enter the first number: ')
        y = input('Enter the second number: ')
        value = x / y
        print "x/y is", value
    except ZeroDivisionError as e:
        print("Invalid input, Please try again.")
    else:
        break