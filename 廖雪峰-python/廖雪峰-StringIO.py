# -*- coding: utf-8 -*-
"""StringIO 顾名思义就是在内存中读写 str"""

__author__ = 'JetLi'

"""要把 str 写入 StringIO，我们需要先创建一个 StringIO，然后，像文件一
样写入即可"""


import StringIO

s = StringIO.StringIO()
s.write('www.baidu.com\r\n')
s.write('news.realsil.com.cn')
s.seek(0)
print '*' * 20
print s.tell()
print s.read()

print s.getvalue()