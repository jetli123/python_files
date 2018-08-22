# -*- coding: utf-8 -*-
"""堡垒机环境在一定程度上提升了运营安全级别，但同时也提高了日常运维成本，作为管理的中转
设备，社和针对业务服务器的管理请求都会经过此节点，比如SSH 协议，首先运维人员在办公电脑通过SSH
协议登录堡垒机，在通过堡垒机SSH 跳转到所有的业务服务器进行维护操作："""
#

# 我们可以利用 paramiko 的invoke_shell 机制来实现通过堡垒机实现服务器操作，原理是 SSHClient.connect
# 到堡垒机后开启一个新的SSH回话（session），通过新的会话运行“ssh user@IP” 去实现远程执行命令的操作。

import paramiko
# import os
import sys
# import time

# 设置堡垒机信息
blip = "192.168.1.23"  # 定义堡垒机信息
bl_user = "root"
bl_password = "system#111"

# 设置业务服务器信息
hostname = "192.168.1.21"  # 定义业务服务器信息（通过堡垒机登录）
username = "root"
password = "admin@122"

# 设置登录前端口、标志串、登录日志信息
port = 22
pass_info = '\'s password: '  # 输入服务器密码前的标志串
paramiko.util.log_to_file('C:\Users\JETLi\Desktop\system_login.log')

# 开始登录堡垒机
ssh = paramiko.SSHClient()  # ssh 登录堡垒机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 没有本地主机秘钥的策略
ssh.connect(hostname=blip, username=bl_user, password=bl_password)

channel = ssh.invoke_shell()  # 开启会话，开启命令调用
channel.settimeout(10)  # 会话命令执行超时时间，单位为秒

# 开始登录业务主机
buff = ''
resp = ''
channel.send('ssh '+username+'@'+hostname+'\n')  # 执行 ssh 登录业务主机
while not buff.endswith(pass_info):  # ssh 登录的提示信息判断，输入串尾含有“\'s password:”时退出循环
    try:
        resp = channel.recv(9999)
    except Exception as e:
        print 'Error info:%s connection time.' % (str(e))
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
    # buff.find(str) # 返回字符串的索引位置，找不到为 -1
    if not buff.find('yes/no') == -1:  # 输入串尾含有“yes/no”时发送“yes”并回车
        channel.send('yes\n')
        buff = ''

channel.send(password+'\n')  # 发送业务主机密码

buff = ''
while not buff.endswith('# '):  # 输出串尾为“#”时说明检验通过并退出while 循环
    resp = channel.recv(9999)  #
    if not resp.find(pass_info) == -1:  # 输出串尾含有“\'s password: ” 时说明密码不正确，需要重新输入
        print 'Error info: Authentication failed.'
        channel.close()  # 关闭连接对象后退出
        ssh.close()
        sys.exit()
    buff += resp

channel.send('ifconfig\n')  # 认证通过后发送 ifconfig 命令来查看结果
buff = ''
try:
    while buff.find('# ') == -1:
        resp = channel.recv(9999)
        buff += resp
except Exception as e:
    print "Error info:"+str(e)

print buff  # 打印输出串
channel.close()
ssh.close()
