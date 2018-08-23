#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""本示例通过 Fabric 的env 对象定义网关模式，即俗称的中转、堡垒机环境。
定义格式为“env.gateway='192.168.1.23'”，其中IP“192.168.1.23”为堡垒机IP，再结合任务
函数实现目标主机文件上传与执行的操作，详细源码如下：
"""

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm


env.user = 'root'
env.gateway = '192.168.1.23'  # 定义堡垒机IP，作为文件上传、执行的中转设备
env.hosts = ['192.168.1.21', '192.168.1.22']
# 假如所有主机密码都不一样，可以通过env.passwords 字典变量一一指定
env.password = {
    'root@192.168.1.21:22': 'admin@123',
    'root@192.168.1.22:22': 'admin@456',
    'root@192.168.1.23:22': 'admin@789'  # 堡垒机账号信息
}

lpackpath = '/home/install/lnmp0.9.tar.gz'  # 本地安装包路径
rpackpath = '/tmp/install'  # 远程安装包路径


@task
def put_task():
    run("mkdir -p /tmp/install")
    with settings(warn_only=True):  # put (上传)出现异常时继续执行，非终止
        result = put(lpackpath, rpackpath)  # 上传安装包
    if result.failed and not confirm("put file failed, Continue[Y/N]?"):  # 获得提示信息确认
        abort("Aborting file put task!")  # 出现异常时，确认用户是否继续，（Y 继续）


@task
def run_task():  # 执行远程命令，安装lnmp 环境
    with cd("/tmp/install"):
        run("tar -zxvf lnmp0.9.tar.gz")
        with cd("lnmp0.9/"):  # 使用with 继续继承 /tmp/install 目录位置状态
            run("./centos.sh")


@task
def go():  # 上传、安装组合
    put_task()
    run_task()

# 示例通过简单的配置 env.gateway='192.168.1.23'就可以轻松实现堡垒机环境的文件上传及执行，相比 paramiko的实现
# 方法简洁了很多，编写的任务函数完全不用考虑堡垒机环境，配置env.gateway 即可。
