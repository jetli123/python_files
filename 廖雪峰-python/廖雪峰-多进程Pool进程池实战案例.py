# -*- coding: utf-8 -*-
from multiprocessing import Pool
import os
import time

# os.walk的参数如下:

# os.walk(top, topdown=True, onerror=None, followlinks=False)
# 其中：
# - top是要遍历的目录。
# - topdown是代表要从上而下遍历还是从下往上遍历。
# - onerror可以用来设置当便利出现错误的处理函数(该函数接受一个OSError的实例作为参数)，设置为空则不作处理。
# - followlinks表示是否要跟随目录下的链接去继续遍历，要注意的是，os.walk不会记录已经遍历的目录，
# 所以跟随链接遍历的话有可能一直循环调用下去。

# os.walk返回的是一个3个元素的元组 (root, dirs, files) ，分别表示遍历的路径名，
# 该路径下的目录列表和该路径下文件列表。注意目录列表和文件列表不是具体路径，
# 需要具体路径(从root开始的路径)的话可以用 os.path.join(root,dir) 和 os.path.join(root,dir) 。


def getFile(path):
    # 获取目录下的文件list
    fileList = []
    for root, dirs, files in os.walk(path):
        for i in files:
            if i.endswith('.txt') or i.endswith('.py'):
                fileList.append(os.path.join(root, i))
    return fileList

print getFile(r'G:\Python27\Scripts')