# -*- coding: utf-8 -*-
"""psutil 是一个跨平台库，轻松实现获取系统进程和系统利用率（CPU、内存、
磁盘、网络等）信息，实现了同等命令行工具，如ps、top、lsof、netstat、ifconfig、who
df、kill、free、nice、ionice、iostat、iostop、uptime、pidof、tty、taskset、pmap"""
__author__ = 'JetLi'

import psutil
from datetime import datetime
import re


# (1) CPU信息
''' 获取系统性能信息 '''
# Linux 系统CPU利用率有以下几个部分:
# User Time, 执行用户进程的时间百分比
# System Time, 执行内核进程和中断的时间百分比
# Wait IO, 由于IO等待而使CPU处于idle(空闲)状态的时间百分比
# Idle, CPU 处于idle状态的时间百分比
# 还可以获得CPU的硬件信息，比如CPU的物理个数和逻辑个数,

# 显示CPU完整信息
print '显示CPU完整信息:', psutil.cpu_times()

# 需要显示所有逻辑CPU信息加上变量 percpu=True
print '所有逻辑CPU信息:', psutil.cpu_times(percpu=True)

# 显示某个逻辑CPU信息的某一项
print '内核进程和中断的时间百分比：%s' % psutil.cpu_times(percpu=True)[1].system

# 获取单项数据信息，如用户
print '执行用户进程的时间百分比: %s' % psutil.cpu_times().user

# 获取CPU的逻辑个数，默认logical=True4
print 'CPU逻辑个数：%d' % psutil.cpu_count()
# 4

# 获取CPU的物理个数
print 'CPU物理个数：%d' % psutil.cpu_count(logical=False)
# 2

# (2) 内存信息
'''获取物理内存大小 psutil.virtual_memory()'''
# 物理内存total 值： free -m |grep Mem |awk '{print $2}'
# 物理内存used 值： free -m |grep Mem |awk '{print $3}'
# Linux 系统内存利用率信息：
# total: 内存总数
# used: 已使用的内存数
# free: 空闲内存数
# buffers: 缓冲使用数
# cache: 缓存使用数
# swap: 交换分区使用数

# 获取内存完整信息
mem = psutil.virtual_memory()
print mem
# svmem(total=4195807232L, available=1283956736L, percent=69.4, used=2911850496L, free=1283956736L)
print '物理内存total值为：%dM' % (mem.total/1024/1024)
print '物理内存used值为：%dM' % (mem.used/1024/1024)
print '物理内存available值为：%dM' % (mem.available/1024/1024)
print '物理内存使用百分比为：%d%%' % (mem.percent)

'''获取 SWAP 分区信息'''
print 'SWAP 分区信息:', psutil.swap_memory()
# sswap(total=8389660672L, used=3111817216L, free=5277843456L, percent=37.1, sin=0, sout=0)

# (3) 磁盘信息
'''获取磁盘完整信息'''
print '磁盘完整信息：', psutil.disk_partitions()
# sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed')
# sdiskpart(device='F:\\', mountpoint='F:\\', fstype='NTFS', opts='rw,fixed')
# sdiskpart(device='G:\\', mountpoint='G:\\', fstype='NTFS', opts='rw,fixed')
# sdiskpart(device='H:\\', mountpoint='H:\\', fstype='NTFS', opts='rw,fixed')
# sdiskpart(device='D:\\', mountpoint='D:\\', fstype='', opts='cdrom')
# sdiskpart(device='E:\\', mountpoint='E:\\', fstype='', opts='cdrom'),

'''磁盘利用率 '''
print '具体磁盘利用率信息：', psutil.disk_usage('C:\\')  # 获取分区的使用情况
# sdiskusage(total=73295458304L, used=29888671744L, free=43406786560L, percent=40.8)

'''磁盘IO信息 '''
# 获取磁盘总的 IO 个数、读写信息
print '磁盘总IO信息：', psutil.disk_io_counters()
# 获取单个分区IO个数、读写信息
print '磁盘单个分区IO信息：', psutil.disk_io_counters(perdisk=True)

# (4) 网络信息
# 系统网络信息包括：
#   bytes_sent=(发送字节数)、bytes_recv=(接收字节数)、packets_sent=(发送数据包数)、packets_recv=(接收数据包数)
'''获取网络信息'''
# 获取网络总的IO信息、默认 pernic=False
print '网络总IO信息：', psutil.net_io_counters()
# snetio(bytes_sent=13922695L, bytes_recv=118019496L, packets_sent=105092L, packets_recv=182207L,
# errin=0L, errout=0L, dropin=0L, dropout=0L)

# 获取每个网口的IO信息
print '每个网口的IO信息：', psutil.net_io_counters(pernic=True)

# (5) 其它系统信息
'''获取当前登录系统用户信息'''
print '当前登录用户信息：', psutil.users()
# [suser(name='JetLi~Pactera%RHELOS', terminal=None, host='0.0.0.0', started=1524624320.0, pid=None)]

#############################################################################################
"""                      -*-  总结：获取登录时间 -*-                   """
start_time = psutil.users()
start_times = psutil.users()[0]
print datetime.fromtimestamp(start_times.started).strftime("%Y-%m-%d %H:%M:%S")
# [suser(name='JetLi~Pactera%RHELOS', terminal=None, host='0.0.0.0', started=1524624320.0, pid=None)]
lst = re.compile(r'.*?started=(.*?), pid.*?]$')  # 查找时间戳字符串
ac = lst.match(str(start_time)).groups()  # 将start_time 转换为字符串格式 str(start_time)
timestamps = float(ac[0])  # 匹配出的字符串转换为 浮点数，float()
# 将timestamp 新纪元开始当前的秒数, 转换成日期格式
login_time = datetime.fromtimestamp(timestamps).strftime("%Y-%m-%d %H:%M:%S")
print '用户登录系统时间：%s' % login_time  # 2018-04-25 10:45:20
##############################################################################################

'''获取开机时间，以Linux 时间戳格式返回'''
print '开机时间戳为：', psutil.boot_time()
# 方法二 获取开机时间
aa = psutil.boot_time()
print '系统开机时间：', datetime.fromtimestamp(aa).strftime("%Y-%m-%d %H:%M:%S")
