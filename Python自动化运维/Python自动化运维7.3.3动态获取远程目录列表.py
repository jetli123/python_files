#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""本示例使用“@task”修饰符标志入口函数go() 对外部课件，配合“@runs_once”修饰符接收用户输入，
最后调用 worktask() 任务函数实现远程命令执行"""
from fabric.api import *


env.user = 'root'
env.hosts = ['127.0.0.1', '192.168.10.236']
env.password = 'centos@2018'

@runs_once  # 主机遍历过程中，只有一台触发此函数
def input_raw():
    return prompt("please input directory name: ", default="/home")  # 获取用户标准输入信息，类似input()


def worktask(dirname):
    run("ls -l "+dirname)


@task  # 限定只有 go 函数对 fab 命令课件
def go():
    getdirname = input_raw()
    worktask(getdirname)

# 该示例实现了一个动态输入远程目录名称，再获取目录列表里的功能，由于我们只要求输入一次，再显示所有
# 主机上该目录的列表信息，调用了一个子函数 input_raw() 同时配置@runs_once 修饰符来达到此目的