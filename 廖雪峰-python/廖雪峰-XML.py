# -*- coding: utf-8 -*-
"""
DOM 会把整个 XML 读入内存，
解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
SAX 是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自
己处理事件.
"""
# 在 Python 中使用 SAX 解析 XML 非常简洁，通常我们关心的事件是
# start_element， end_element 和 char_data，准备好这 3 个函数，然后就可
# 以解析 xml 了
from xml.parsers.expat import ParserCreate


"""<a href="/">python</a>"""
"""
    会产生 3 个事件：
1. start_element 事件，在读取<a href="/">时；
2. char_data 事件，在读取 python 时；
3. end_element 事件，在读取</a>时。
"""


class DefaultSaxHandler(object):

    def start_element(self, name, attrs):
        print 'sax:start_element: %s, attrs: %s' % (name, str(attrs))

    def end_element(self, name):
        print 'sax:end_element: %s' % name

    def char_data(self, text):
        print 'sax:char_data: %s' % text

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
