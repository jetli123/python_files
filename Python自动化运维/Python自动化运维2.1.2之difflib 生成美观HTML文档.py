# -*- coding: utf-8 -*-
"""采用HtmlDiff()类 的make_file()方法 就可以生成美观的HTML 文档"""

import difflib

file1 = """file1:
Download the file for your platform.
If you're not sure which to choose,
learn more about
installing packages."""

file1_lines = file1.splitlines()

file2 = """file2:
Download The file for your Platform.
Oh! I understand.
Learn more about too
installing packages."""

file2_lines = file2.splitlines()

d = difflib.HtmlDiff()
diff_file = d.make_file(file1_lines, file2_lines)
print diff_file

# with open(r'G:/PyCharm/untitled/diff.html', 'w') as f:
#     f.write(diff_file)