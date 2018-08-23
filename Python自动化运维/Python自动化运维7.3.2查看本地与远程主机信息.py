#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
本示例调用local() 方法执行本地（主控端）命令，添加“@runs_once”修饰符保证该任务
函数只执行一次。调用run() 方法执行远程命令。
"""
from fabric.api import *

env.user = 'root'
env.hosts = ['192.168.1.2', '192.168.1.3']
env.password = 'admin@123'


@runs_once  # 查看本地系统信息，当有多台主机时只运行一次
def local_task():
    local("uname -a")


def remote_task():
    with cd("/data/logs"):  # "with" 的作用是让后面的表达式的语句继承当前状态，
        run("ls -l")  # 实现"cd /data/logs && ls -l"的效果

# 通过 fab 命令分别调用 local_task 任务函数运行结果：
# fab -s file.py local_task  默认登录192.168.1.2 主机执行"uname -a"指令，不会去 192.168.1.3上执行
# fab -s file.py remote_task 两台主机都去登录和执行cd /data/logs && ls -l 指令
