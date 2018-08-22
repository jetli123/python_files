# -*- coding: utf-8 -*-
"""
    如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下
来，第二步就是解析该 HTML 页面，看看里面的内容到底是新闻、图
片还是视频。
"""
from urllib import urlopen
import re

a = urlopen('http://www.sina.com.cn')
data = a.read()
# print 'Status:', a.status, a.reason
# for k, v in data.getheaders():
#     print '%s: %s' % (k, v)
print 'Data:', data.decode('utf-8')

# with open('G:\\PyCharm\\untitled\\jet.txt', 'w+') as f:
#     f.write(data)

# with open(r'G:\\PyCharm\\untitled\\jet.txt') as e:
#     a = re.compile('.*<a href="(http.*?)".*?</a>.*')
#     for line in e.readlines():
#         line = line.strip()
#         b = a.match(line)
#         if b:
#            print b.groups()