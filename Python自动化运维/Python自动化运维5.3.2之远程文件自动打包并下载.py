# -*- coding: utf-8 -*-
"""在Linux系统集群运营当中，时常需要批量远程执行 Linux命令，并且双向同步文件的操作。
本示例通过使用spawn() f方法执行ssh、scp命令的思路来实现，具体实现源码如下："""

import pexpect
import sys

ip = "192.168.1.21"  # 定义目标主机
user = "root"  # 目标主机用户
passwd = "H6DSY#*$df32"  # 目标主机密码
target_file = "/data/logs/nginx_access.log"  # 目标主机nginx 日志文件

child = pexpect.spawn('/usr/bin/ssh', [user+'@'+ip])  # 运行ssh 命令
fout = file('mylog.txt', 'w')  # 输入、输出日志下入mylog.txt 文件
child.logfile = fout

try:
    child.expect('(?i)password')  # 匹配password 字符串, (?i)表示不区分大小写
    child.sendline(passwd)
    child.expect('#')
    child.sendline('tar -czf /data/nginx_access.tar.gz '+target_file)  # 打包nginx 日志文件

    child.expect('#')
    print child.before
    child.sendline('exit')
    fout.close()
except pexpect.EOF:  # 定义 EOF 异常处理
    print("expect EOF")
except pexpect.TIMEOUT:  # 定义TIMEOUT 异常处理
    print("expect TIMEOUT")

# 启动scp 远程拷贝命令，实现将打包好的nginx 日复制至本地 /home 目录
child = pexpect.spawn('/usr/bin/scp', [user+'@'+ip+':/data/nginx_access.tar.gz', '/home/'])
fout = file("mylog.txt", 'a')
child.logfile = fout

try:
    child.expect('(?i)password')
    child.sendline(passwd)
    child.expect(pexpect.EOF)  # 匹配缓冲区 EOF （结尾），保证文件复制正常完成
except pexpect.EOF:
    print "expect EOF"
except pexpect.TIMEOUT:
    print "expect TIMEOUT"