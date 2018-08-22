# -*- coding: utf-8 -*-
import re
import sys
import filecmp
import os
import shutil
fileoldlist = []


def compareme(dir1, dir2):
    getdir = filecmp.dircmp(dir1, dir2)
    get_source_list = getdir.left_only
    get_diff_list = getdir.diff_files
    [fileoldlist.append(os.path.abspath(os.path.join(dir1, x))) for x in get_source_list]
    [fileoldlist.append(os.path.abspath(os.path.join(dir1, x))) for x in get_diff_list]
    if getdir.common_dirs > 0:
        for item in getdir.common_dirs:
            compareme(os.path.abspath(os.path.join(dir1, item)), os.path.abspath(os.path.join(dir2, item)))
    return fileoldlist


def main():
    if len(sys.argv) > 2:
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
    else:
        print "Usage:", sys.argv[0], "sourcedir backupdir"
        sys.exit()

    source_files = compareme(dir1, dir2)
    print source_files
    dir1 = os.path.abspath(dir1)
    print dir1
    dir2 = os.path.abspath(dir2)
    print dir2
    destination_files = []
    createdir_bool = False
    for item in source_files:

        destination_dir = re.sub(dir1, dir2, item)

        destination_files.append(destination_dir)
        # 如果没有子目录直接跳到
        if os.path.isdir(item):
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                createdir_bool = True
    print destination_files

    if createdir_bool:
        destination_files = []
        source_files = compareme(dir1, dir2)
        for item in source_files:
            destination_dir = re.sub(dir1, dir2, item)
            destination_files.append(destination_dir)
    # print source_files

    copy_pair = zip(source_files, destination_files)
    for item in copy_pair:
        if os.path.isfile(item[0]):
            shutil.copyfile(item[0], item[1])


if __name__ == '__main__':
    main()
