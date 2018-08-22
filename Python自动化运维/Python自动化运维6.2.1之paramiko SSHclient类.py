# -*- coding: utf-8 -*-
"""SSHClient 类是SSH 服务会话的高级表示，该类封装了传输（transport）、通道（channel）及SFTPClient的校验、
建立的方法，通常用于远程命令"""
import paramiko

client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect('ssh.example.com')
stdin, stdout, stderr = client.exec_command('ls -l')
client.close()
# SSHClient 类常用方法：

# 1.connect 方法实现了远程SSH 连接并校验。
# connect(self, hostname, port=22, username=None, password=None, pkey=None, key_filename=None,
# timeout=None, allow_agent=True, look_for_keys=True, compress=False)
# 参数说明：
# hostname（str 类型），连接的模板主机地址；
# port（int 类型），连接目标主机的端口，默认为22；
# username（str 类型），校验的用户名（默认为当前的本地用户名）；
# password（str 类型），密码用于身份校验或解锁秘钥；
# pkey（PKey 类型），私钥方式用于身份验证；
# key_filename（str or list(str) 类型），一个文件名或文件名的列表，用于私钥的身份验证；
# timeout（float 类型），一个可选的超时时间（以秒为单位）的TCP 连接；
# allow_agent（bool类型），设置为False时用于禁用连接到 SSH代理；
# look_for_keys（bool 类型），设置为False 时用来禁用在 ~/.ssh 中搜索秘钥文件；
# compress（bool类型），设置为True 时打开压缩。

# 2.exec_command 方法
# 远程命令执行方法，该命令的输入与输出流为标准输入（stdin）、输出（stdout）、错误（stderr）的Python文件对象，方法定义：
# exec_command(self, command, bufsize=-1)
# 参数说明：
# command(str 类型)，执行的命令串；
# bufsize(int 类型)，文件缓冲区大小，默认为-1（不限制）。

# 3.load_system_host_keys 方法
# 加载本地公钥校验文件，默认为~/.ssh/known_hosts，非默认路径需要手工指定，方法定义：
#  load_system_host_keys(self, filename=None)
# 参数说明：
# filename(str 类型)，指定远程主机公钥记录文件。

# 4.set_missing_host_key_policy 方法
# 设置连接的远程主机没有本地主机秘钥或HostKeys 对象时的策略，目前支持三种，分别是:
# 1> AutoAddPolicy，自动添加主机名及主机秘钥到本地 HostKeys对象，并将其保存，不依赖 load_system_host_keys() 配置，
# 即使 ~/.ssh/known_hosts 不存在也不产生影响；
# 2> RejectPolicy，自动拒绝未知的主机名和秘钥，依赖 load_system_host_keys() 的配置；
# 3> WariningPolicy，用于记录一个未知的主机秘钥的Python 警告，并接受它，功能上与AutoAddPolicy 相似，但未知主机会有告警。
# 使用方法：
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())