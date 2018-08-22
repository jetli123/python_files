# -*- coding: utf-8 -*-
"""
expect 方法有两个非常棒的成员：before 与 after
    before: 保存了最近匹配成功之前的内容
    after：保存了最近匹配成功之后的内容
"""
__author = 'JetLI'
__history__ = '2018/07/22 23:21'

import pexpect
import sys


child = pexpect.spawn('ssh root@192.168.200.28')
fout = file('/root/abc.txt', 'w')
child.logfile = fout

child.expect(["password:"])
child.sendline("centos")
print "before:"+child.before
print "after:"+child.after

# read相关方法：
# 下面这些输入方法的作用都是向子程序发送响应命令，可以理解成代替了我们标准输入的键盘
"""
send(self, s) 发送命令，不回车
sendline(self, s='') 发送命令，回车
sendcontrol(self, char) 发送控制字符，如child.sendcontrol('c) 等价于“ctrl+c”
sendeof() 发送 eof"""

# 例如：
"""
#!/bin/bash/env python
# -*- coding:utf-8 -*-
  'this is login server'''
__author__ = 'JetLi'
__history__ = '2018/07/24 14:34'

import pexpect


child = pexpect.spawn('ssh', ['root@127.0.0.1'], timeout=5)
fout = file("/root/3.txt", "w")
child.logfile = fout

child.expect("password:")
child.sendline("centos")
print "before:"+child.before  --root@127.0.0.1's
print "after:"+child.after    -- password:
child.expect('#')
child.sendline('ls -lrt')
child.expect('#')
child.expect(pexpect.TIMEOUT)
"""