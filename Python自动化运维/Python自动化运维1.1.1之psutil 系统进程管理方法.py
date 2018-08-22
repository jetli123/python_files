# -*- coding: utf-8 -*-
"""获得进程启动时间，查看或设置CPU亲和度，内存使用率，IO信息，socket连接，线程数"""
import psutil
import json
from datetime import datetime

# 一、进程信息

# 列出所有进程PID
print '所有进程PID:', (psutil.pids())  # [0, 4, 424, 676, 768, 776, 824, 872, 880, 888, 988, 468, 652, 948, 1060]
# 实例化一个Process对象，参数为一个进程PID
p1 = psutil.Process(psutil.pids()[-3])
# 获取进程名
print '进程名:', p1.name()  # pycharm.exe
# 进程bin路径
# print '进程bin路径', p1.exe()  # D:\PyCharm\bin\pycharm.exe
# 进程工作绝对路径
# print '进程工作绝对路径', p1.cwd()  # D:\PyCharm\jre\jre\bin
# 进程状态
print '进程状态:', p1.status()  # running
# 进程创建时间，时间戳格式
print '进程创建时间:', p1.create_time()
# 通过datetime 模块转换为时间日期格式
print '进程创建时间:', datetime.fromtimestamp(p1.create_time())  # 2018-04-29 22:05:18

# 进程UID信息
# print p1.uids()
# print p1.gids()  # Windows 下没有此项　Linux 下有这个方法

L1 = psutil.pids()
L2 = []
for i in L1:
    p = psutil.Process(i)
    L2.append(p.name())

with open(r'D:/Python27/python file/0429.txt', 'w') as f:
    f.write(json.dumps(L2))

# 进程CPU时间信息，包括user,system两个CPU时间
print '进程CPU时间信息:', p1.cpu_times()

# 进程内存利用率
print '进程内存利用率:', p1.memory_percent()
# 进程内存rss,vms 信息
print '进程内存rss,vms 信息:', p1.memory_info()
# 进程I/O信息，包括读写I/O数及字节数
print '进程I/O信息:', p1.io_counters()
# 返回打开进程的 socket的nameduples列表，包括fs, family, laddr等信息
print '打开进程的 socket的nameduples列表', p1.connections()
# 进程开启的线程数
print '进程开启的线程数:', p1.num_threads()
