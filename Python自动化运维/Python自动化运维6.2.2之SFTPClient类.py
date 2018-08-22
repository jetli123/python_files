# -*- coding: utf-8 -*-
"""SFTPClient 作为一个SFTP 客户端对象，根据SSH传输协议的sftp 回话，实现远程文件操作，比如文件上传、
下载、权限、状态等操作，下面介绍SFTPClient 类的常用方法。"""

import paramiko


# 1.from_transport 方法
# 创建一个已连通的SFTP 客户端通道，方法定义：
# from_transport(cls, t)
# 参数说明：
# t（Transport），一个已通过验证的传输对象。
# 例子说明：
# t = paramiko.Transport(("192.168.1.22", 22))
# t.connect(username="root", password="ksksksksk")
# sftp = paramiko.SFTPClient.from_transport(t)

# 2.put 方法
# 上传本地文件到远程 SFTP 服务端，方法定义：
# put(self, localpath, remotepath, callback=None, confirm=True)
# 参数说明：
# localpath(str 类型)，需上传的本地文件（源）；
# remotepath(str 类型)，远程路径（目标）；
# callback(function(int, int)), 获取以接收的字节数及总传输字节数，以便回调函数调用，默认为None;
# confirm(bool 类型)，文件上传完毕后是否调用stat() 方法，以便确认文件的大小。
# 例子说明：
# localpath = '/home/access.log'
# remotepath = '/data/logs/access.log'
# sftp.put(localpath, remotepath)

# 3.get 方法
# 从远程 SFTP 服务端下载文件到本地，方法定义：
# get(self, remotepath, localpath, callback=None)
# 参数说明：
# remotepath(str 类型)，需下载的远程文件（源）；
# localpath(str 类型)，本地路径（目标）；
# callback(function(int, int))，获取已接收的字节数及总传输字节数，以便回调函数调用，默认为None。
# 例子说明：
# remotepath = '/data/logs/access.log'
# localpath = '/home/access.log'
# sftp.get(remotepath, localpath)

# 4.其他方法
# SFTPClient 类其他常用方法：
# mkdir，在SFTP 服务器端创建目录，如 sftp.mkdir("/home/userdir", 0755)。
# remove，删除SFTP服务器端指定目录，如 sftp.remove("/home/userdir")。
# rename，重命名SFTP 服务器端文件或目录，如 sftp.rename("/home/test.sh", "/home/testfile.sh")。
# stat，获取远程SFTP 服务器端指定文件信息，如 sftp.stat("/home/testfile.sh")。
# listdir，获取远程 SFTP服务器端指定目录列表，以Python的列表（list）形式返回，如 sftp.listdir("/home")。