# -*- coding: utf-8 -*-
"""
    IP地址规划是网络设计中非常重要的环节，规划的好坏直接影响路由协议算法的效率，
包括，网络性能、可扩展性等方面，在这个过程中，免不了要计算大量的IP地址，包括网段、
网络掩码、广播地址、子网数、IP 类型等。
"""
from IPy import IP

# 通过version()方法，区分出IPv4 和 IPv6
print IP('10.0.0.0/8').version()  # 4 代表IPv4类型
# 4
print IP('::1').version()  # 6 代表IPv6类型
# 6

# 通过指定的网段输出该网段的IP 个数及所有IP 地址清单
ip = IP('192.168.0.0/16')
print '192.168.0.0/16网段共有地址：', ip.len()
# 65536个地址

# 输出 192.168.0.0/16 网段所有IP地址 到文件中
# with open(r'D:/Python27/python file/ip.txt', 'w') as f:
#     for x in ip:
#         f.write(str(x) + '\n')

# IP 类型 iptype()
ip1 = IP('192.168.1.20')
print '192.168.1.20地址类型：', ip1.iptype()
# PRIVATE  为私网类型
ip2 = IP('8.8.8.8')
print '8.8.8.8地址类型：', ip2.iptype()
# PUBLIC  为公网类型

# 反向解析地址格式 reverseNames()
print '192.168.1.20反向解析地址格式：', ip1.reverseNames()
# 20.1.168.192.in-addr.arpa.
