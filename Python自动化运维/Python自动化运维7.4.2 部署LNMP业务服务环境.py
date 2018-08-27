#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""业务上线之前最关键的一项任务便是环境部署，往往一个业务涉及很多中应用环境，比如
Web、DB、PROXY、CACHE等，本示例通过 env.roledefs定义不同主机角色，再使用“@roles('webservers')”
修饰符绑定到对应任务函数，实现不同角色主机的部署差异："""
from fabric.api import *
from fabric.colors import *
env.user = 'root'
env.rolesdefs = {  # 定义业务角色分组
    'webservers': ['192.168.1.21', '192.168.1.22'],
    'dbservers': ['192.168.1.23']
}
env.passwords = {
    'root@192.168.1.21:22': 'root@123',
    'root@192.168.1.22:22': 'root@456',
    'root@192.168.1.23:22': 'root@789'
}


@roles('webservers')  # webtask 任务函数引用 'webservers' 角色修饰符
def webtask():  # 部署nginx php php-fpm 等环境
    print yellow("Install nginx php php-fpm...")
    with settings(warn_only=True):
        run("yum -y install nginx")
        run("yum -y install php-fpm php-mysql php-mbstring php-xml php-mcrypt php-gd")
        run("chkconfig --levels 235 php-fpm on")
        run("chkconfig --levels 235 nginx on")


@roles('dbservers')  # dbtask 任务函数引用'dbservers' 角色修饰符
def dbtask():  # 部署mysql 环境
    print yellow("Install Mysql...")
    with settings(warn_only=True):
        run("yum -y install mysql mysql-server")
        run("chkconfig --levels 235 mysqld on")


@roles('webservers', 'dbservers')  # publictask 任务函数同事引用两个角色修饰符
def publictask():  # 部署公共类环境，如 epel、ntp 等
    print yellow("Install epel ntp...")
    with settings(warn_only=True):
        run("rpm -Uvh http://d1.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm")
        run("yum -y install ntp")


def deploy():
    execute(publictask)
    execute(webtask)

# 本示例通过角色来区别不同业务服务环境，分别部署不同的程序包，我们只需要一个 python脚本就可以完成不同业务
# 环境的定制