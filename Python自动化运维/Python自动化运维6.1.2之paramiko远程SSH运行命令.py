# -*- coding: utf-8 -*-
import paramiko

hostname = '10.223.76.179'
username = 'systemuser'
password = 'dhlr@bj123'
paramiko.util.log_to_file(r'C:\Users\JETLi\Desktop\syslogin.log')  # 发送paramiko 日志到 syslogin.log 文件

ssh = paramiko.SSHClient()  # 创建一个ssh 客户端 client 对象
# ssh.load_system_host_keys()  # 获取客户端host_keys, 默认 ~/.ssh/known_hosts，非默认路径需指定
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 没有本地主机秘钥的策略
ssh.connect(hostname=hostname, username=username, password=password)  # 创建ssh 连接
stdin, stdout, stderr = ssh.exec_command('ls -altr')  # 调用远程执行命令方法 exec_command()
print stdout.read()  # 打印命令执行结果，得到python 列表形式，可以使用 stdout.readlines()
ssh.close()  # 关闭ssh 连接