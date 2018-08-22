# -*- coding: utf-8 -*-


from drawing import colors
from drawing import dras
from drawing import module
from drawing import shapes

__author__ = 'Jetli'


def test():
    print 'Now time is : "%s"' % colors.nows()
    print 'The digit is: %s' % dras.pp()

test()


def test1():
    module.hello()

test1()


def test3():
    a = shapes.add3(10, 34, int)
    b = shapes.int3()
    print a
    print b

test3()
