# -*- coding: utf-8 -*-
import fileinput


def process(string):
    print('Process: ', string)


for line in fileinput.input('G:\\PyCharm\\untitled\\abd.txt'):
    process(line)
