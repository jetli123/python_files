# -*- coding: utf-8 -*-
# 利用FileInput将CRLF文件转为LF
__author__ = 'JetLi'

import sys
import fileinput

for line in fileinput.input(inplace=True):
    if line[-2:] == '':
        line += line
    sys.stdout.write(line)
