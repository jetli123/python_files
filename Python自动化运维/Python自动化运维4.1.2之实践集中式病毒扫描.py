# -*- coding: utf-8 -*-
"""针对不同业务环境定制扫描策略，
比如扫描对象，描述模式、扫描路径、调度频率等。
实现架构：
    1.首先业务服务器开启clamd 服务（监听3310 端口），
    2.管理服务器启用多线程对指定的服务集群进行扫描
    3.扫描模式、扫描路径会传递到 clamd，
    4.最后返回扫描结果给管理服务器。
"""

# 本次实践通过ClamdNetworkSocker() 方法实现与业务服务器建立扫描 socker 连接
# 在通过启动不同扫描方式实施病毒扫描并返回结果。
__metaclass__ = type

import pyclamd
import time
from threading import Thread


class Scan(Thread):
    def __init__(self, IP, scan_type, file):
        """构造方法，参数初始化"""
        # 两种方法： 下面和 super 函数
        # Thread.__init__(self)
        super(Scan, self).__init__()
        self.IP = IP
        self.scan_type = scan_type
        self.file = file
        self.connstr = ""
        self.scanresult = ""

    def run(self):
        """多进程 run 方法"""
        try:
            cd = pyclamd.ClamdNetworkSocket(self.IP, 3310, timeout=3)  # 创建网络套接字连接对象
            # void = open(r'D:/EICAR', 'w')
            # void.write(cd.EICAR())
            # void.close()

            if cd.ping():  # 探测连通性
                self.connstr = self.IP + " connection [OK]"
                # 重载 clamd 病毒特征库，建议更新病毒库后做 reload() 操作
                # cd.reload()
                # 选择不同的扫描模式
                if self.scan_type == "contscan_file":
                    self.scanresult = "{0}\n".format(cd.contscan_file(self.file))
                elif self.scan_type == "multiscan_file":
                    self.scanresult = "{0}\n".format(cd.multiscan_file(self.file))
                elif self.scan_type == "scan_file":
                    self.scanresult = "{0}\n".format(cd.scan_file(self.file))
                time.sleep(1)  # 线程挂起 1 秒
            else:
                self.connstr = self.IP + " ping error,exit"
                return
        except Exception as e:
            self.connstr = self.IP + " " + str(e)


IPs = ['192.168.10.189', '192.168.10.2']  # 扫描主机列表
scantype = "multiscan_file"  # 指写扫描模式， 支持 multiscan_file、contscan_file、scan_file
scanfile = "/usr/local"  # 指定扫描路径
i = 1

threadnum = 2  # 指定启动线程数
scanlist = []  # 存储扫描Scan 类线程对象列表

for ip in IPs:
    currp = Scan(ip, scantype, scanfile)  # 创建扫描Scan 类对象，参数（IP，扫描模式，扫描路径）
    scanlist.append(currp)  # 追加对象到列表

    if i % threadnum == 0 or i == len(IPs):  # 当达到指定的线程数或IP 列表数后启动、退出线程
        for task in scanlist:
            task.start()  # 启动线程
        for task in scanlist:
            task.join()  # 等待所有子进程退出，并输出扫描结果
            print task.connstr  # 打印服务器连接信息
            print task.scanresult  # 打印扫描结果
        scanlist = {}
    i += 1

# 通过EICAR() 方法生成一个带有病毒特征的文件 /tmp/EICAR

