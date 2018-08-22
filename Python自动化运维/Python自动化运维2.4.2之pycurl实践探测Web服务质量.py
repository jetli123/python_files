# -*- coding: utf-8 -*-
"""探测的两个标准：
1. 服务的可用性，不出现404 页面未找到，500 页面错误等；
2. 服务响应速度，静态类文件下载时间控制在毫秒级，动态GUI 为秒级。

本示例：使用 pycurl的 setopt() 和 getinfo() 方法"""

import os, sys
import time
import pycurl

URL = "http://172.16.73.51:1081/#/login"  # 探测的目标URL
c = pycurl.Curl()  # 创建一个 Curl 对象
c.setopt(pycurl.URL, URL)  # 定义请求的URL 常量
c.setopt(pycurl.CONNECTTIMEOUT, 5)  # 定义请求连接的等待时间
c.setopt(pycurl.TIMEOUT, 5)  # 定义请求超时时间
c.setopt(pycurl.NOPROGRESS, 1)  # 屏蔽下载进度条
c.setopt(pycurl.FORBID_REUSE, 1)  # 完成交互后强制断开连接，不重用 noprogress
c.setopt(pycurl.MAXREDIRS, 1)  # 指定 HTTP 重定向的最大数为1
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)  # 设置保存DNS 信息的时间为30秒
# 创建一个文件对象，以 "wb" 方式打开，用来存储返回的http 头部及页面内容
indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt", "wb")
c.setopt(pycurl.WRITEHEADER, indexfile)  # 将返回的HTTP HEADER 定向到 indexfile 文件对象
c.setopt(pycurl.WRITEDATA, indexfile)  # 将返回的 HTML 内容定向到 indexfile 文件对象
try:
    c.perform()  # 提交请求
except Exception, e:
    print "connection error:"+str(e)
    indexfile.close()
    c.close()
    sys.exit()

NAMELOOKUP_TIME = c.getinfo(pycurl.NAMELOOKUP_TIME)  # 获取DNS 解析时间
CONNECT_TIME = c.getinfo(pycurl.CONNECT_TIME)  # 获取建立连接时间
PRETRANSFER_TIME = c.getinfo(pycurl.PRETRANSFER_TIME)  # 获取从建立连接到准备传输所消耗的时间
STARTTRANSFER_TIME = c.getinfo(pycurl.STARTTRANSFER_TIME)  # 获取从建立连接到传输开始消耗的时间
TOTAL_TIME = c.getinfo(pycurl.TOTAL_TIME)  # 获取传输的总时间
HTTP_CODE = c.getinfo(pycurl.HTTP_CODE)  # 获取 HTTP 状态码
SIZE_DOWNLOAD = c.getinfo(pycurl.HTTP_CODE)  # 获取下载数据包大小
HEADER_SIZE = c.getinfo(pycurl.HEADER_SIZE)  # 获取HTTP 头部大小
SPEED_DOWNLOAD = c.getinfo(pycurl.SPEED_DOWNLOAD)  # 获取平局下载速度

# 打印传输相关数据
print "HTTP 状态码: %s" % (HTTP_CODE)
print "DNS 解析时间： %.2f ms" % (NAMELOOKUP_TIME * 1000)
print "建立连接时间： %.2f ms" % (CONNECT_TIME * 1000)
print "准备传输时间： %.2f ms" % (PRETRANSFER_TIME * 1000)
print "传输开始时间： %.2f ms" % (STARTTRANSFER_TIME * 1000)
print "传输结束总时间： %.2f ms" % (TOTAL_TIME * 1000)
print "下载数据包大小： %d bytes/s" % (SIZE_DOWNLOAD)
print "HTTP 头部大小： %d byte" % (HEADER_SIZE)
print "平均下载速度： %d bytes/s" % (SPEED_DOWNLOAD)
# 关闭文件及 Curl 对象
indexfile.close()
c.close()