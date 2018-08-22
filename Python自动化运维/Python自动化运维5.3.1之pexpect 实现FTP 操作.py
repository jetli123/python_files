# -*- coding: utf-8 -*-
"""我们常用FTP 协议实现自动化、集中式的文件备份，要求做到账号登录、文件上传与下载、退出
等实现自动化操作，本示例使用pexpect 模块的spawnu() 方法执行FTP 命令，通过 expect() 方法
定义匹配的输出规则，sendline() 方法执行相关的FTP交互命令等，详细源码如下："""

from __future__ import unicode_literals  # 使用 Unicode 编码
import pexpect
import sys

child = pexpect.spawnu('ftp ftp.openbsd.org')  # 运行 ftp 命令
child.expect('(?i)name .*: ')  # (?i) 表示后面的字符串正则匹配忽略大小写
child.sendline('anonymous')  # 输入 ftp 账号信息
child.expect('(?i)password')  # 匹配密码输入提示
child.sendline('pexpect@sourceforge.net')  # 输入 ftp 密码
child.expect('ftp> ')
child.sendline('bin')  # 启用二进制传输模式
child.expect('ftp> ')
child.sendline('get robots.txt')  # 下载 robots.ext 文件
child.expect('ftp> ')
sys.stdout.write(child.before)  # 输出匹配“ftp> ” 之前的输入与输出
print("Escape character is '^]'.\n")
sys.stdout.write(child.after)
sys.stdout.flush()
# 调用 interact() 让出控制权，用户可以继续当前的回话手工控制子程序，默认输入“^]”字符跳出
child.interact()
child.sendline('bye')
child.close()