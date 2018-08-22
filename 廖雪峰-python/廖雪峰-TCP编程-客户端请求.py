# -*- coding:utf-8 -*-
"""
    Socket 是网络编程的一个抽象概念。通常我们用一个 Socket 表示“打开
了一个网络链接”，而打开一个 Socket 需要知道目标计算机的 IP 地址和
端口号，再指定协议类型即可。
"""
__author__ = 'JetLi'

# 创建 TCP 连接时，
# 主动发起连接的叫客户端，
# 被动响应连接的叫服务器
__version__ = '1.2.19'
import socket

"""客户端"""
# 创建一个 socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
# 注意参数是一个 tuple，包含地址和端口号
s.connect(('www.sina.com.cn', 80))
# AF_INET 指定使用 IPv4 协议，如果要用更先进的 IPv6，就指定为 AF_INET6。
# SOCK_STREAM 指定使用面向流的 TCP 协议，

"""建立 TCP 连接后，我们就可以向新浪服务器发送请求，要求返回首页
的内容："""
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection:close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    # 每次最多接收 1k 字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)
"""接收数据时，调用 recv(max)方法，一次最多接收指定的字节数，因此，
在一个 while 循环中反复接收，直到 recv()返回空数据，表示接收完毕，
退出循环。
"""
# 当我们接收完数据后，调用 close()方法关闭 Socket，这样，一次完整的网络通信就结束了：
# 关闭连接:
s.close()

# 接收到的数据包括 HTTP 头和网页本身，我们只需要把 HTTP 头和网页
# 分离一下，把 HTTP 头打印出来，网页内容保存到文件：
header, html = data.split(b'\r\n\r\n', 1)
print header.decode('utf-8')
# 把接收的数据写入文件:
with open('D:/Python software/python file/sina.html', 'wb') as f:
    f.write(html)


#  练习：
m = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
m.connect(('www.hao123.com', 80))
m.send(b'GET / HTTP/1.1\r\nHost: www.hao123.com\r\nConnection:close\r\n\r\n')
buffers = []
while True:
    n = m.recv(1024)
    if n:
        buffers.append(n)
    else:
        break

values = b''.join(buffers)
m.close()
headers, htmls = values.split(b'\r\n\r\n', 1)
print headers.decode('utf-8')
with open('D:/Python software/python file/sax.html', 'wb') as e:
    e.write(htmls)
