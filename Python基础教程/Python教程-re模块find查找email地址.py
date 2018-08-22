# -*- coding: utf-8 -*-
# 查找 Email 中的发件人信息
import re
import fileinput

a = re.compile('From: (.*) <.*?>$')

for line in fileinput.input():
    m = a.match(line)
    if m:
        print m.group(1)
