# -*- coding: utf-8 -*-
"""difflib 实现文件的差异对比，可以输出可读性较强的HTML 文档"""
import difflib

# 定义字符串 test1
test1 = """text1:
I love you.
And I love you too.
Oh my god! Rearly?
It's true."""

# 定义字符串 test2
test2 = """text2:
I Love you.
And I Love You.
Oh my god! Rearly?
It's true."""
test1_lines = test1.splitlines()  # 以行进行分隔，以便进行对比
test2_lines = test2.splitlines()

d = difflib.Differ()  # 创建Differ() 对象
diff = d.compare(test1_lines, test2_lines)  # 采用compare方法对字符串进行比较
# print list(diff)
print '\n'.join(list(diff))  # diff 对象是个 generator 惰性循环，需要list() 去遍历