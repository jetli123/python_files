# -*- coding: utf-8 -*-
"""ClamAV 是一款免费开放的防毒软件，软件和病毒库又社区发布，
主要为 Linux、Unix 提供病毒扫描、查杀服务。"""
# pyClamad 是一个 python 第三方模块，可以让python 直接使用 ClamAV病毒扫描守护进程 clamd,
# 来实现一个高效的病毒扫描检测功能

# -*- pyClamad 安装如下：
# 1、客户端（病毒扫描源）安装步骤
# yum install clamav clamd clamav-update  # 安装 clamavp 相关程序包
# chkconfig --level 235 clamd on  # 添加扫描守护进程 clamd 系统服务，开机启动
# /usr/bin/freshclam   # 更新病毒库建议配置到 crontab 中定期更新
# setenforce 0   # 关闭 SELinux ，避免远程扫描时提示无权限问题

# 更新守护进程监听 IP 配置文件，根据不同环境自行修改监听的 IP，“0.0.0.0” 为监听所有主机 IP
# sed -i -e '/^TCPAddr/{ s/127.0.0.1/0.0.0.0/; }'  /etc/clamd.conf
# /etc/init.d/clamd start  # 启动扫描守护进程

# 2、主控端部署 pyClamad 环境步骤
# wget http://xael.org/norman/python/pyclamd/pyClamd-0.3.4.tar.gz
# tar -zxvf pyClamd-0.3.4.tar.gz
# cd pyClamd-0.3.4
# python setup.py install

# 模块常用方法说明
# __init__(self, host='127.0.0.1', post=3310, timeout=None)方法， 是ClamdNetworkSocket类的初始化方法，
# host：为连接主机IP；
# port：为连接端口，默认为3310，与 /etc/clamd.conf 配置文件中的TCPSocket 参数要保持一致；
# timeout: 为连接超时时间。

# contscan_file(self, file)方法，实现扫描指定文件或目录，在扫描时发生错误或发现病毒将不终止，
# file(string)类型：为指定的文件或目录的绝对路径。

# multiscan_file(self, file)方法，实现多线程扫描指定的文件或目录，多核环境速度更快，
# 在扫描时发生错误或发现病毒将不终止，
# file(string)类型：为指定的文件或目录的绝对路径

# scan_file(self, file)方法，实现扫描指定的文件或目录，在扫描时发现错误或发现病毒将终止，
# file(string)类型：为指定的文件或目录的绝对路径

# shutdown(self)方法，实现强制关闭 clamd 进程并退出。

# stats(self)方法，获取Clamscan 的当前状态。

# reload(self)方法，强制重载 clamd 病毒库特征，扫描前建议做 reload 操作。

# EICAR(self)方法，返回EICAR 测试字符串，即生成具有病毒特征的字符串，便于测试。
