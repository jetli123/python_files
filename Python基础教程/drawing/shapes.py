# -*- coding: utf-8 -*-
__all__ = ['y', 'add3', 'int2']


def int2(x, base=2):
    def aa():
        return int(x, base)
    return aa


def int3():
    y = int2('01110111')
    return y()


def add3(x, c, f):
    assert isinstance(c, int), 'The second of parameter that input %s is not int!' % c
    return f(x) + f(c)


if __name__ == "__main__":
    print 'This is main of module for <shapes.py>!'
