# -*- coding: utf-8 -*-
"""pxssh 是pexpect 的派生类，针对在ssh 会话操作上再做一层封装，提供与基类更加直接的操作方法。"""

# pxssh 类定义：
# class pexpect.pxssh.pxssh(timeout=30, maxread=2000, searchwindowsize=None, logfile=None, cwd=None, env=None)
# pxssh 常用的三个方法如下：
# 1. login() 建立ssh 连接
# 2. logout() 断开连接
# 3. prompt() 等待系统提示符，用于等待命令执行结果。
"""
  下面使用pxssh 类实现一个 ssh连接远程主机并执行命令的示例。
1.首先使用 login() 方法与远程主机建立连接，
2.再通过 sendline() 方法发送执行的命令，
3.prompt() 方法等待命令执行结束且出现系统提示符，
4.使用 logout()方法断开连接。"""

from pexpect import pxssh
import getpass
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
try:
    s = pxssh.pxssh()
    hostname = raw_input("hostname: ")
    username = raw_input("username: ")
    password = getpass.getpass('please input password: ')  # 接收密码输入
    s.login(hostname, username, password)  # 建立ssh 连接
    s.sendline('uptime')  # 运行uptime 命令
    s.prompt()  # 匹配系统提示符
    print s.before  # 打印出现系统提示符前的命令输出
    s.sendline('ls -l')
    s.prompt()
    print s.before
    s.sendline('df')
    s.prompt()
    print s.before
    s.logout()  # 断开ssh 连接
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print str(e)