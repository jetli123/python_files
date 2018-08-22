#!/usr/bin/env python
# -*- coding:utf-8 -*-

import difflib
import sys
import logging
logging.basicConfig(level=logging.INFO)


try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
except Exception as e:
    logging.exception(e)
#    print("Error:"+str(e))
    print "Usage: simple.py filename1 filename2"
    sys.exit()


def readline(filename):

    try:
        fileHandle = open(filename, 'rb')
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:
        print 'Read file Error:'+str(error)
        sys.exit()


if textfile1 == '' or textfile2 == '':
    print 'Usage: simple.py filename1 filename2'
    sys.exit()

text1_lines = readline(textfile1)
text2_lines = readline(textfile2)

d = difflib.HtmlDiff()
print d.make_file(text1_lines, text2_lines)
