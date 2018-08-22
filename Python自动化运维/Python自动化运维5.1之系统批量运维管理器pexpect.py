# -*- coding: utf-8 -*-
"""pexpect 可以理解成Linux 下的expect 的Python封装，通过pexpect 我们可以实现
对 ssh、ftp、passwd、telnet 等命令行进行自动交互，而无需人工干涉来达到自动化的目的。
比如，我们可以模拟一个FTP登录时的所有交互，包括输入主机地址、用户名、密码、上传
文件等，待出现异常我们还可以进行尝试自动处理。"""

# 源码安装，笔者采用 GitHub 平台的项目托管源
# wget https://github.com/pexpect/pexpect/releases/download/3.0/pexpect-3.0.tar.gz -O pexpect-3.0.tar.gz
# tar -zxf pexpect-3.0.tar.gz
# cd pexpect-3.0
# python setup.py install

# 实现一个简单的SSH 自动登录
import pexpect

child = pexpect.spawn('scp', ['/root/install.log', 'root@127.0.0.1:/tmp/'], timeout=8)  # spawn 启动scp 程序
fout = file('/root/mylog.log', 'w')
child.logfile = fout  #  写到日志中
child.expect('Are you sure you want to continue connecting?')  # 匹配定义的字符串
child.sendline('yes')  # 匹配后发送字符串 yes 回应
child.expect("root@127.0.0.1's password: ")  # expect 方法等待子程序产生的输出，判断是否匹配定义的字符串 'Password:'
child.sendline('centos\n')  # 匹配后则发送密码串进行回应
child.expect(pexpect.EOF)  # 指向缓冲区尾部
