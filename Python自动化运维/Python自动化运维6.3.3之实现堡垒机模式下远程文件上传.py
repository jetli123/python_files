# -*- coding: utf-8 -*-
"""实现堡垒机模式下的文件上传，原理是通过paramiko 的 SFTPClient 将文件从办公设备上传至堡垒机指定的临时目录，
如/tmp ， 在通过SSHClient 的invoke_shell 方法开启ssh 会话，执行 scp 命令，将/tmp 下的指定文件复制到目标业务服务器上：
"""

#  系统管理员---SFTPClient.put--->堡垒机（/tmp/）<----scp---->业务服务器集群
#           <--------------------

# 本示例具体使用 sftp.put() 方法上传文件至堡垒机临时目录，在通过send() 方法执行 scp命令，将堡垒机临时目录下的
# 文件复制到目标主机，详细的实现源码如下：

import paramiko
import sys
import os
import time


bl_ip = "172.16.230.67"  # 定义堡垒机地址
bl_user = "root"  # 登录堡垒机登录用户
bl_password = "centos"  # 定义堡垒机登录密码
hostname = "192.168.1.21"  # 定义业务服务器地址
username = "root"  # 定义业务服务器登录用户
password = "admin@123"  # 定义业务服务器登录密码

tmp_dir = "/root"  # 堡垒机临时目录
remote_dir = "/data"
local_path = "C:\Users\JetLi\Desktop\Email.py"  # 本地源文件路径
tmp_path = tmp_dir+"/Email.py"  # 堡垒机临时路径
remote_path = remote_dir+"/nginx_access_hd.tar.gz"  # 业务主机目录路径

port = 22
password_info = '\'s password: '
paramiko.util.log_to_file('C:/Users/JetLi/Desktop/sys_login.log')
# sftp 方式上传文件到 堡垒机
t = paramiko.Transport((bl_ip, port))
t.connect(username=bl_user, password=bl_password)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(local_path, tmp_path)  # 上传本地源文件到堡垒机临时路径
sftp.close()
# ssh 方式登录堡垒机
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #  定义主机密钥策略，忽略本地密钥
ssh.connect(hostname=bl_ip, username=bl_user, password=bl_password)

channel = ssh.invoke_shell()  # 在堡垒机上开启 ssh 会话
channel.settimeout(10)  # 设置指令执行超时时间

buff = ''
resp = ''
# scp 中转目录文件到目标主机
channel.send('scp '+tmp_path+' '+username+'@'+hostname+':'+remote_path+'\n')
# 判断是否匹配到 '\'s password: '，没有匹配到在进入循环中，在判断是否需要记住密钥
while not buff.endswith(password_info):
    try:
        resp = channel.recv(9999)
    except Exception as e:
        print 'Errorm info: %s connection time.' % (str(e))
        channel.close()
        ssh.close()
        sys.exit()
    buff += resp
    # 判断第一次需要记住密钥
    if not buff.find('yes/no') == -1:
        channel.send('yes\n')
        buff = ''

channel.send(password+'\n')

# 判断输入密码后，是否scp 拷贝完成出现 #，没有出现，在判断是否出现密码提示符，密码输入是否错误
buff = ''
while not buff.endswith('# '):
    resp = channel.recv(9999)
    if not buff.find(password_info) == -1:
        print 'Error info: Authentication failed.'
        channel.close()
        ssh.close()
        sys.exit()

    buff += resp
print buff
channel.close()
ssh.close()