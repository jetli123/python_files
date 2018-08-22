# -*- coding: utf-8 -*-
"""
  本次实践通过python-nmap 实现一个高效的端口扫描工具，与定时作业 crontab及邮件结合告警组合，
可以很好地帮助我们及时发现异常开放的高危端口。
  该工具也可以作为业务服务端口的可用性探测，例如扫描 192.168.1.20-25 网段 Web 服务端口 80 是否处于
open 状态。实践所采用的 scan() 方法的 arguments 参数指定为“ -v -PE -p '+端口' ”,
-v ：表示启用细节模式，可以返回非 up 状态主机清单；
-PE：表示采用TCP 同步扫描（TCP SYN）方式；
-p：指定扫描端口范围。
  程序输出部分采用了三个 for 循环体，第一层遍历扫描主机，第二层为遍历协议，第三层为遍历端口，
最后输出主机状态。"""

# 如下：
import sys
import nmap

scan_row = []
input_data = raw_input('Please input host and port: ')
for i in input_data.split(' '):
    scan_row.append(i)
if len(scan_row) != 2:
    print "Input errors, example \"192.168.1.0/24 80, 443, 22\""
    sys.exit(0)
hosts = scan_row[0]  # 接收用户输入的主机
port = scan_row[1]  # 接收用户输入的端口

try:
    nm = nmap.PortScanner() # 创建端口扫描对象
except nmap.PortScannerError:
    print('Nmap not found', sys.exc_info()[0])
    sys.exit(0)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(0)

try:
    # 调用扫描方法，参数指定扫描主机 hosts, nmap 扫描命令行参数 arguments
    nm.scan(hosts=hosts, arguments=' -v -sS -p '+port)
except Exception as e:
    print "Scan error:"+str(e)

for host in nm.all_hosts():  # 遍历扫描主机
    print('-------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname())) # 输出主机及主机名
    print('State : %s' % nm[host].state())  # 输出主机状态， 如 up、down
    for proto in nm[hosts].all_protocols():  # 遍历扫描协议，如 tcp、udp
        print('--------------------------------------------------')
        print('Protocol : %s' % proto)  # 输出协议名

        lport = nm[host][proto].keys()  # 获取协议的所有扫描端口
        lport.sort()  # 端口列表排序
        for port in lport:  # 遍历端口及输出端口与状态
            print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

# 其中主机输入支持所有表达方式，如 www.qq.com 、192.168.1.*、192.168.1.1-20、192.168.1.0/24 等
# 端口输入格式：如 80，443，22、 80，22-443
"""
{
'nmap': {
    'scanstats': {'uphosts': u'1', 'timestr': u'Wed Jun 20 22:01:20 2018', 'downhosts': u'0', 'totalhosts': u'1', 'elapsed': u'6.25'},
    'scaninfo': {u'tcp': {'services': u'22,111,3306', 'method': u'syn'}},
    'command_line': u'nmap -oX - -p 22,3306,111 -sV 192.168.10.189'
        },
'scan': {
    u'192.168.10.189': {
        'status': {'state': u'up', 'reason': u'localhost-response'},
        'hostname': u'node1.com',
        u'tcp': {
            3306: {'state': u'open', 'reason': u'syn-ack', 'name': u'mysql'},
            22: {'state': u'open', 'reason': u'syn-ack', 'name': u'ssh'},
            111: {'state': u'open', 'reason': u'syn-ack', 'name': u'rpcbind'}
                }
                        }
        }
}
"""