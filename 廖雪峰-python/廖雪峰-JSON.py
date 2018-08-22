# -*- coding: utf-8 -*-
"""JSON 表示的对象就是标准的 JavaScript 语言的对象，JSON 和 Python
内置的数据类型对应如下"""

"""
JSON 类型  Python 类型
{}         dict
[]         list
"string"   str
1234.56    int 或 float
true/false True/False
null       None
"""

import json

d = dict(name='Jet', age=20, score=99)
f = open('G:\\PyCharm\\untitled\\ff1.txt', 'wb')
f.write(json.dumps(d))
f.close()

f2 = open('G:\\PyCharm\\untitled\\ff3.txt', 'wb')
json.dump(d, f2)
f2.close()

# 要把 JSON 反序列化为 Python 对象，用 loads()或者对应的 load()方法，
# 前者把 JSON 的字符串反序列化，后者从 file-like Object 中读取字符
# 串并反序列化：

# 方法1：打开文件，读取序内容，通过 json.loads() 函数反序列化成 Python 格式的dict
f3 = open('G:\\PyCharm\\untitled\\ff3.txt', 'rb')
print json.loads(f3.read())
f3.close()
# {u'age': 100, u'score': 100, u'name': u'Jet'}

# 方法2：直接通过json.load() 函数直接读取文件内容，反序列化成 Python 格式的dict
f4 = open('G:\\PyCharm\\untitled\\ff3.txt', 'rb')
print json.load(f4)
f4.close()
