# -*- coding: utf-8 -*-
import re


# test = raw_input('Enter your string: ')
# if re.match(r'^\d{3}\s?-\s?\d{3,8}$', test):
#     print 'OK...'
# else:
#     print 'Failed!'

"""拆分字符串"""

# 用正则表达式切分字符串比用固定的字符更灵活
print(re.split(r'[ ]+', 'a b  c'))
print(re.split(r'[ ,]+', 'a ,b  ,,c,d'))
print(re.split(r'[\s,;]+', 'a, ;b,c; d ;e'))

# re.split(,maxsplit=2) ,maxsplit= 表示字符串最多可以分隔的次数
print(re.split(r'[ ,]+', 'alpha, beta,,,,gamma  delta', maxsplit=2))

"""分组"""
# 用()表示的就是要提取的分组（Group）
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-232043')
print(m.group(1), m.group(2))

t = '19:05:30'
s = re.match(r"^(0[0-9]|1[0-9]|2[0-3]|[0-9]):"
             r"(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9]):"
             r"(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$",
             t)
print(s.groups())

"""贪婪匹配"""

# 正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。
# 例子1：
print(re.match(r'^(\d+)(0*)$', '1023000').groups())
"""
    由于\d+采用贪婪匹配，直接把后面的 0 全部匹配了，结果 0*只能匹配
空字符串了。
"""
# 必须让\d+ 采用非贪婪匹配，才能把后面的 0 匹配出来，
# 加个? 就可以让\d+采用非贪婪匹配

# 例子2：
print(re.match(r'^(\d+?)(0*)$', '1023000').groups())

"""编译"""

# 1.  编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# 2.  用编译后的正则表达式去匹配字符串。

re_telephone = re.compile(r"^(\d{3})-(\d{3,8})$")
print(re_telephone.match('010-303049').groups())
# 编译后生成 Regular Expression 对象，由于该对象自己包含了正则表达
# 式，所以调用对应的方法时不用给出正则字符串。

"""返回给定模式的所有匹配"""
# re.findall() 列出字符串中模式的所有匹配项
pat = '[a-zA-Z]+'
text = '"Hm... Err -- are you sure?" he said, sounding insecure.'
print('列出字符串中模式的所有匹配项:', re.findall(pat, text))

# 在字符串中查找所有标点符号
let = '[,.?\-"]+'
print(re.findall(let, text))

"""根据包含正则表达式的字符串创建模式对象"""
# re.compile()
# 模式对象本身也有查找匹配的函数，例如： re.match(pattent, string)
# （pattent, 是用字符串表示的正则表达式） 等价于 pattent.match(string), pattent 是用 compile()创建的模式对象
ce = re.compile('(\d+)\-(\d{3,8})$')
ab = ce.match('010-939483')
print(ab.group(1))
print(ab.group(2))

# 练习 获取Email 地址
# someone@gmail.com
# bill.gates@microsoft.com
a = input('Enter your Email Address: ')
b = re.match(r'([a-z]*?)\.?([a-z]+)(\@[a-z]+\.com$)', a)
print(b.groups())

# 练习2 程序获取Email 发件人信息
# From: Foo Fie <foo@bar.com>
f = re.compile('From: (.*) <.*?>$')
d = open(r'G:\\PyCharm\\untitled\\abd.txt')
for line in d.readlines():
    try:
        m = f.match(line)
        if m:
            print(m.group(1))
    finally:
        d.close()

# 将字符串中所有 pat的匹配项用repl 替换
# re.sub(pat, repl, string[, count=0])
pat = '{name}'
string = 'Dear {name}'
repl = 'Mr. Gumby'
print('pat 替换为repl:', re.sub(pat, repl, string))
