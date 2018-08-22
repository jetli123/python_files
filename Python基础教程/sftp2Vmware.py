# -*- coding: utf-8 -*-
""""""
import paramiko
import sys

hostname = '192.168.10.236'
username = 'root'
password = 'centos@2018'
port = 22

local_path = r'D:\Python27\python file\xiaoshuo.py'
sys_path = '/root/xiaoshuo.py'

t = paramiko.Transport((hostname, port))
t.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(local_path, sys_path)
# sftp.get(sys_path, local_path)
sftp.close()

# paramiko.util.log_to_file(r"C:\Users\JetLi\Desktop\sys1.log")
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname=hostname, username=username, password=password)
# stdin, stdout, stderr = ssh.exec_command(r"wget https://pypi.python.org/packages/source/F/Fabric/Fabric-1.8.2.tar.gz --no-check-certificate")
# print stdout.read()
# print stdout2.read()
# print stdout3.read()
# print stdout4.read()
# ssh.close()
# sys.exit()