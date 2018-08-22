# -*- coding: utf-8 -*-
"""
Fabric 是基于Python 实现的SSH命令行工具，简化了SSH的应用程序部署及系统管理任务，它提供了系统基础的
操作组件，可以实现本地或远程shell 命令，包括命令执行、文件上传、下载及完整执行日志输出等功能。
Fabric 在paramiko 的基础上做了更高一层的封装，操作起来会更加简单。官网：http://www.fabric.org
"""

# Fabric 的安装
# Fabric 支持pip、easy_install 或源码安装方式，很方便解决包依赖的问题，具体安装命令如下：
# pip install fabric
# easy_install fabric
# Fabric 依赖第三方的 setuptools、PyCrypto、paramiko 包的支持，源码安装步骤如下：

# yum -y install python-setuptools
# wget https://pypi.python.org/packages/source/F/Fabric/Fabric-1.8.2.tar.gz --no-check-certificate
# tar -zxvf Fabric-1.8.2.tar.gz
# cd Fabric-1.8.2
# python setup.py install

# 在cmd下执行：
#
# 1、pip install PyCrypto
# 2、pip install paramiko
# 3、pip install fabric==1.10.2    # 注意当前最高版本为2.0.1，版本太高内部会有不满足依赖，
# from fabric.api import * 时会报错：ImportError: No module named api

# 官网提供简单的入门示例：
from fabric.api import run

def host_type():
    run('uname -s')


# 外部调用：fab -u root -p centos@2018 -H 192.168.10.236 -f file1.py host_type
# 外部调用：fab -u root -p centos@2018 -H 192.168.10.236 -- 'ifconfig && uname -a'