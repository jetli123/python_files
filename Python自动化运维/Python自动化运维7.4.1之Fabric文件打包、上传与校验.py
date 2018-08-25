#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""我们时常做一些文件包分发的工作，实施步骤一般是先压缩打包，在批量上传至目标服务器，最后做一致性校验。
本案例通过put() 方法实现文件的上传，通过对比本地与远程主机文件的 md5，最终实现文件一致性校验。"""

from fabric.api import *
from fabric.context_managers import *
from fabric.contrib.console import confirm


env.user = 'root'
env.hosts = ['192.168.1.21', '192.168.1.22']
env.passwords = [
    "root@192.168.1.21:22", 'centos@2018',
    "root@192.168.1.22:22", "dhlr@2091"]


@task
@runs_once
def tar_task():  # 本地打包任务函数，只执行一次
    with lcd("/data/logs"):
        local("tar -zcvf access.tar.gz access.log")

@task
def put_task():  # 上传文件任务函数
    run("mkdir -p /data/logs")
    with cd("/data/logs"):
        with settings(warn_only=True):  # put(上传)出现异常时继续执行，非终止
            result = put("/data/logs/access.tar.gz", "/data/logs/access.tar.gz")
        if result.failed and not confirm("put file failed, Continue[Y/N]?"):
            abort("Aborting file put task!")  # 出现异常时，确认用户是否继续，（Y 继续）

@task
def check_task():  # 校验文件任务函数
    with settings(warn_only=True):
        # 本地local 命令需要配置 capture=True 才能捕获返回值
        lmd5 = local("md5sum /data/logs/access.tar.gz", capture=True).split(' ')[0]
        rmd5 = run("md5sum /data/logs/access.tar.gz").split(' '[0])
    if lmd5 == rmd5:  # 对比本地及远程文件 md5 信息
        print "OK"
    else:
        print "ERROR"

# 本示例通过定义三个功能任务函数，分别实现文件的打包、上传、校验功能，且三个功能相互独立，
# 可分开运行，如：
# fab -f simple4.py tar_task  -- 文件打包
# fab -f simple4.py put_task  -- 文件上传
# fab -f simple4.py check_task  -- 文件校验

# 当然，我们也可以组合在一起运行，再添加一个 任务函数go，代码如下：


@task
def go():
    execute(tar_task)
    execute(put_task)
    execute(check_task)
