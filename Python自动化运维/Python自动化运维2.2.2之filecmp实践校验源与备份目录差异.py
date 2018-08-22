# -*- coding: utf-8 -*-
"""有时候我们无法确认备份目录与源目录文件是否一致，包括源目录中
的新文件或目录、更新文件或目录有无成功同步，定期进行校验，
没有成功则希望有针对性地进行补备份。"""

# 本实例使用了 filecmp 模块的left_only、diff_files 方法递归获取源目录更新项。
# 再通过 shutil.copyfile、os.makedirs 方法对更新项进行复制，最终保持一致状态。

import os
import sys
import filecmp
import re
import shutil
holderlist = []


def compareme(dir1, dir2):  # 递归获取更新项函数
    dircomp = filecmp.dircmp(dir1, dir2)
    only_in_one = dircomp.left_only  # 源目录新的文件或目录
    diff_in_one = dircomp.diff_files  # 不匹配文件，源目录文件已发生变化
    # dirpath = os.path.abspath(dir1)  # 定义源目录绝对路径

    # 将更新文件名或目录追加到 holderlist
    [holderlist.append(os.path.abspath(os.path.join(dir1, x))) for x in only_in_one]
    [holderlist.append(os.path.abspath(os.path.join(dir1, x))) for x in diff_in_one]
    if len(dircomp.common_dirs) > 0:  # 判断是否存在相同子目录，以便递归
        for item in dircomp.common_dirs:  # 递归子目录
            compareme(os.path.abspath(os.path.join(dir1, item)),
                      os.path.abspath(os.path.join(dir2, item)))
    return holderlist


def main():  # 标准输入获取目录函数
    if len(sys.argv) > 2:  # 要求输入源目录与备份目录
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
    else:
        print "Usage:", sys.argv[0], "datadir backupdir"
        sys.exit()

    source_files = compareme(dir1, dir2)  # 对比源目录与备份目录
    dir1 = os.path.abspath(dir1)

    if not dir2.endswith('/'):
        dir2 += '/'  # 备份目录路径加 '/' 符号

    dir2 = os.path.abspath(dir2)
    destination_files = []
    createdir_bool = False

    for item in source_files:  # 遍历返回的差异文件或目录清单
        # 将所有的 dir1 目录名称替换为 dir2 名称
        destination_dir = re.sub(dir1, dir2, item)
        # 获取 全是以dir2为名称的带绝对路径的文件列表
        destination_files.append(destination_dir)
        if os.path.isdir(item):
            # 对比目录，找到在 dir2 不存在的目录创建
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)  # 创建目录
                createdir_bool = True  # 再次调用compareme 函数标记

    # 下面在重新对比，不考虑目录了，因为目录已经创建了，重新获取所有的绝对路径的文件列表
    if createdir_bool:  # 重新调用compareme 函数，重新遍历新创建目录的内容
        destination_files = []
        # source_files = []
        source_files = compareme(dir1, dir2)  # 调用compareme 函数
        for item in source_files:  # 获取源目录差异路径清单，并且对应替换成备份目录
            destination_dir = re.sub(dir1, dir2, item)
            destination_files.append(destination_dir)
    
    print "update item:"
    print source_files  # 输出更新项列表清单
# 拷贝 **********************************
    copy_pair = zip(source_files, destination_files)  # 将源目录与备份目录文件清单替换成元组
    for item in copy_pair:
        if os.path.isfile(item[0]):  # 判断是否为文件，是则进行复制操作
            shutil.copyfile(item[0], item[1])
# *****************************************
if __name__ == '__main__':
    main()
