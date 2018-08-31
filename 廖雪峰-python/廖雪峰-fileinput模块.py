# -*- coding: utf-8 -*-
import fileinput                         #
                                         #  3
                                         #  4 
# for line in fileinput.input('D:\Python software\python file\module.py'): #  5 
#     print fileinput.filename(), '|', 'Line Number:', fileinput.filelineno(), '|:', line #  6 
                                         #  7 
                                         #  8 
for line in fileinput.input(inplace=True): #  9 
    line = line.rstrip()                 # 10 
    num = fileinput.lineno()             # 11 
    print('%-40s # %2i ' % (line, num))  # 12
    input("Enter any one!")