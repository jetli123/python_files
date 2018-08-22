# -*- coding: utf-8 -*-
""""""
# run 是使用pexpect 进行封装的 调用外部命令的函数，类似于os.system 或 os.popen 方法，
# 不同的是，使用 run() 可以同时获得命令的输出结果及命令的退出状态，函数定义：
# pexpect.run(command, timeout=-1, withexitstatus=False, events=None, extra_args=None,logfile=None, cwd=None, env=None)

# 参数 command 可以是系统已知的任意命令，如果有写绝对路径时将会尝试搜索命令的路径，events 是一个字典，定义了expect及 sendline
# 方法的对应关系，spawn方式的例子如下：
"""
from pexpect import *
child = spawn('scp 2.txt user@example.com:.')
child.expect('(?i)password')
child.sendline('centos')
"""
# 使用 run 函数实现如下：
import pexpect

pexpect.run('scp 1.txt user@example.com:.', events={'(?i)password': 'centos\n'})
