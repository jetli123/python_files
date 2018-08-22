# -*- coding: utf-8 -*-
__author__ = 'JetLi'


def nows():
    import time
    aa = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    return aa


if __name__ == "__main__":
    print 'This is main of module "colors.py"'
