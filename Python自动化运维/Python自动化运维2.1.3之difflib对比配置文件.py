# -*- coding: utf-8  -*-
"""维护多个Nginx配置时，时常对比不同版本配置文件的差异，
使运维人员更加清晰地了解不同版本迭代后的更新项，再以换行符
作为分隔符，调用difflib.HtmlDiff() 生成HTML格式的差异文档"""

import difflib
import sys
import logging
logging.basicConfig(level=logging.INFO)

try:
    testfile1 = sys.argv[1]
    testfile2 = sys.argv[2]
except Exception as e:
    logging.exception("Error:"+str(e))
    print "Usage: simple.py filename1 filename2"
    sys.exit()

def readfile(filename):
    try:
        fileHandle = open(filename, 'rb')
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:
        print('Read file Error:'+str(error))
        sys.exit()

if testfile1 == "" or testfile2 == "":
    print "Usage: simple.py filename1 filename2"
    sys.exit()

text1_lines = readfile(testfile1)
text2_lines = readfile(testfile2)

d = difflib.HtmlDiff()
print d.make_file(text1_lines, text2_lines)