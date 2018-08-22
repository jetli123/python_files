# -*- coding: utf-8 -*-
"""当我们进行代码审计或者校验备份结果时，需要检查原始与目标目录
的文件一致性，标准库filecmp 可以实现文件、目录、遍历子目录的差异
对比功能"""
import filecmp

# filecmp提供了三个操作方法：
# 1.cmp 单文件对比
# 2.cmpfiles 多文件对比
# 3.dircmp 目录对比

# -*- 单文件对比 -*-
'''filecmp.cmp(f1, f2[, shallow])
比较 f1和f2 的文件，相同返回True ,不同返回False，
shallow 默认值为True: 意思是只根据 os.stat()方法返回文件基本信息进行对比，
比如最后访问时间、修改时间、状态改变时间等，会忽略文件内容对比，
shallow 值为False 时： 则 os.stat() 与文件内容同时进行校验。'''

print '两个文件是否相同：', filecmp.cmp("G:/PyCharm/untitled/jet.txt", "G:/PyCharm/untitled/mem.txt")
# False
print '两个文件信息和内容是否相同：', filecmp.cmp("G:/PyCharm/untitled/ff1.txt", "G:/PyCharm/untitled/ff3.txt", False)
# True

# -*- 多文件对比 -*-
'''filecmp.cmpfiles(dir1, dir2, common[, shallow])
对比dir1和dir2目录给定的文件清单, 返回文件名的三个列表，
包括：([匹配]， [不匹配], [错误])'''
# 匹配：包含匹配的文件列表
# 不匹配：反之
# 错误：目录不存在的文件、文件不具备读权限或其他原因导致不能比较的文件清单

print '两个目录的文件对比情况：', filecmp.cmpfiles("G:/PyCharm/untitled", "G:/PyCharm", ['ff1.txt', 'build.txt'])
# ([], [], ['ff1.txt', 'build.txt'])
# ff1.txt 在目录G:/PyCharm中不存在，build.txt 在目录G:/PyCharm/untitled 中不存在，无法比较，所以结果错误

#  -*- 目录对比 -*-
'''dircmp(a, b[,ignore,[,hide]) 类，创建一个目录比较对象，
其中a 和 b 是参加比较的目录名。
ignore:代表文件名忽略的列表，并默认为['RCS', 'CVS', 'tags']
hide: 代表隐藏的列表，默认为[os.curdir, os.pardir]
dircmp 类 可以获得目录比较的详细信息，
如只有在 a 目录中包括的文件、a与b 都存在的子目录、匹配的文件等
同时支持递归'''

# dircmp 提供三个输出报告的方法
# 1. report() , 比较当前指定目录中的内容
# 2. report_partial_closure()，比较当前指定目录及第一级子目录中的内容
# 3. report_full_closure()， 递归比较所有指定目录的内容

# 为输出更加详细的比较结果，dircmp类还提供了以下属性：
# left, 左目录， 如类定义中的 a；
# right, 右目录， 如类定义中的 b；
# left_list, 左目录中的文件及目录列表；
# right_list, 右目录中的文件及目录列表；
# common, 两边目录共同存在的文件或目录；
# left_only, 只在左目录中的文件或目录；
# right_only, 只在右目录中的文件或目录；
# common_dirs, 两边目录都存在的子目录；
# common_files, 两边目录都存在的子文件；
# common_funny, 两边目录都存在的子目录（不同目录类型或os.stat()记录的错误）；
# same_files, 匹配相同的文件；
# diff_files, 不匹配的文件；
# funny_files, 两边目录中都存在，但无法比较的文件；
# subdirs, 将 common_dirs 目录名映射到新的dircmp对象，格式为字典类型。

"""测试"""

a = "G:\Python27\dir1"  # 定义左目录
b = "G:\Python27\dir2"  # 定义右目录
dirobj = filecmp.dircmp(a, b, ['log.txt'])  # 目录比较，忽略log.txt 文件
dirobj.report()
# diff G:\Python27\dir1 G:\Python27\dir2
# Only in G:\Python27\dir1 : ['system.sql']
# Only in G:\Python27\dir2 : ['abc.sql']
# Identical files : ['diff.py', 'jar.txt']
# Common subdirectories : ['a']

dirobj.report_partial_closure()
# diff G:\Python27\dir1 G:\Python27\dir2
# Only in G:\Python27\dir1 : ['system.sql']
# Only in G:\Python27\dir2 : ['abc.sql']
# Identical files : ['diff.py', 'jar.txt']
# Common subdirectories : ['a']

# diff G:\Python27\dir1\a G:\Python27\dir2\a
# Only in G:\Python27\dir1\a : ['c']
# Only in G:\Python27\dir2\a : ['nginx2.conf']
# Identical files : ['nginx1.conf']
# left_list:['a', 'diff.py', 'jar.txt', 'system.sql']
# right_list:['a', 'abc.sql', 'diff.py', 'jar.txt']
# common:['a', 'jar.txt', 'diff.py']

print "left_list:"+str(dirobj.left_list)  # left_list:['a', 'diff.py', 'jar.txt', 'system.sql']
print "right_list:"+str(dirobj.right_list)  # right_list:['a', 'abc.sql', 'diff.py', 'jar.txt']
print "common:"+str(dirobj.common)  # common:['a', 'jar.txt', 'diff.py']
print "left_only:"+str(dirobj.left_only)  # left_only:['system.sql']
print "right_only:"+str(dirobj.right_only)  # right_only:['abc.sql']
print "common_dirs:"+str(dirobj.common_dirs)  # common_dirs:['a']
print "common_files:"+str(dirobj.common_files)  # common_files:['jar.txt', 'diff.py']
print "common_funny:"+str(dirobj.common_funny)  # common_funny:[]
print "same_file:"+str(dirobj.same_files)   # same_file:['diff.py', 'jar.txt']
print "diff_files:"+str(dirobj.diff_files)  # diff_files:[]
print "funny_files:"+str(dirobj.funny_files)  # funny_files:[]
