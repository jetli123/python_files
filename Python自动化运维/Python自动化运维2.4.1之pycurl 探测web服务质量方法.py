# -*- coding: utf-8 -*-
"""pycurl 是一个用C语言写的libcurl Python 实现，支持协议有
FTP、HTTP、HTTPS、TELNET等"""
# 可以理解成Linux 下curl 命令功能的Python 封装，
# 通过pycurl 提供的方法，实现探测Web 服务质量情况，比如：响应的HTTP状态码、请求延时、HTTP头信息、下载速度等
# 利用这些信息可以定位服务响应慢的具体细节。
# pip install pycurl

import pycurl
# 检测安装结果
print pycurl.version
# PycURL/7.43.0.1 libcurl/7.57.0 OpenSSL/1.1.0g zlib/1.2.11 c-ares/1.13.0 libssh2/1.8.0

# 模块常用方法说明：
# pycurl.Curl()类：实现创建一个 libcurl 包的Curl 句柄对象，无参数。
# 1.close()方法：对应 libcurl 包中的 curl_easy_cleanup 方法，无参数，实现关闭，回收Curl 对象。
# 2.perform()方法：对应 libcurl 包中的 curl_easy_perform 方法，无参数，实现Curl 对象请求的提交。
# 3.setopt(option, value)方法：对应libcurl 包中的 curl_easy_setopt 方法，参数 iption 是通过
# libcurl 的常量来指定的，参数 value 的值会依赖option，可以是一个字符串、整型、长整型、文件对象、列表或函数。

c = pycurl.Curl()  # 创建一个 curl 对象
c.setopt(pycurl.CONNECTTIMEOUT, 5)  # 连接的等待时间，设置为0 则不等待
c.setopt(pycurl.TIMEOUT, 5)  # 请求超时时间
c.setopt(pycurl.NOPROGRESS, 0)  # 是否屏蔽下载进度条， 非 0 则屏蔽
c.setopt(pycurl.MAXREDIRS, 5)  # 指定 HTTP 重定向的最大数
c.setopt(pycurl.FORBID_REUSE, 1)  # 完成交互后强制断开连接，不重用
c.setopt(pycurl.FRESH_CONNECT, 1)  # 强制获取新的连接，即替代缓存中的连接
c.setopt(pycurl.DNS_CACHE_TIMEOUT, 60)  # 设置保存DNS 信息的时间，默认为120秒
c.setopt(pycurl.URL, "http://www.baidu.com")  # 指定请求的URL
c.setopt(pycurl.USERAGENT, "Mozilla/5.2 (compatible; MSIE 6.0; Windows NT 5.1;\
SV1; .NET CLR 1.14322; .NET CLR 2.0.50324)")  # 配置请求HTTP头的User-Agent
c.setopt(pycurl.HEADERFUNCTION, getheader)  # 将返回的 HTTP HEADER 定向到回调函数 getheader
c.setopt(pycurl.WRITEFUNCTION, getbody)  # 将返回的内容定向到回调函数 getbody
c.setopt(pycurl.WRITEHEADER, fileobj)  # 将返回的 HTTP HEADER 定向到fileobj 文件对象
c.setopt(pycurl.WRITEDATA, fileobj)  # 将返回的 HTML 内容定向到fileobj 文件对象

# getinfo(option) 方法，对应 libcurl 包中的 curl_easy_getinfo 方法，参数option 是通过 libcurl 的常量来指定的。
b = pycurl.Curl()  # 创建一个 curl 对象
b.getinfo(pycurl.HTTP_CODE)  # 返回的 HTTP 状态码
b.getinfo(pycurl.TOTAL_TIME)  # 传输结束所消耗的总时间
b.getinfo(pycurl.NAMELOOKUP_TIME)  # DNS 解析所消耗的时间
b.getinfo(pycurl.CONNECT_TIME)  # 建立连接所消耗的时间
b.getinfo(pycurl.PRETRANSFER_TIME)  # 从建立连接到准备传输所消耗的时间
b.getinfo(pycurl.STARTTRANSFER_TIME)  # 从建立连接到传输开始消耗的时间
b.getinfo(pycurl.REDIRECT_TIME)  # 重定向所消耗的时间
b.getinfo(pycurl.SIZE_UPLOAD)  # 上传数据包大小
b.getinfo(pycurl.SIZE_DOWNLOAD)  # 下载数据包大小
b.getinfo(pycurl.SPEED_DOWNLOAD)  # 平局下载速度
b.getinfo(pycurl.SPEED_UPLOAD)  # 平局上传速度
b.getinfo(pycurl.HEADER_SIZE)  # HTTP 头部大小
