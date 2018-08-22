# -*- coding: utf-8 -*-
"""下面为 SFTPClient 类的一个完整示例，实现了文件上传、下载、创建与删除目录等，需要注意的是，put 和 get
方法需要指定文件名，不能省略。"""
import paramiko
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

username = "root"
password = "centos"
hostname = "172.16.230.67"
port = 22

try:
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)

    # sftp.put("C:\Users\JetLi\Downloads\psutil-5.4.5.tar.gz", "/root/psutil-5.4.5.tar.gz")  # 上传文件
    # sftp.get("/root/simple.py", "C:\Users\JetLi\Desktop\simple.py")  # 下载文件
    # sftp.mkdir("/home/userdir1", 0755)  # 创建目录
    sftp.rmdir("/home/userdir1")  # 删除目录
    # sftp.rename("/home/test.sh", "/home/testfile.sh")  # 文件重命名
    print sftp.stat("/root/sqlite3.py")  # 打印文件信息
    print sftp.listdir("/home")  # 打印目录列表
    t.close()
except Exception as e:
    print str(e)