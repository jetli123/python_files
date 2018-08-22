# -*- coding: utf-8 -*-
"""通过Python的第三方模块 python-nmap 来实现高效的端口扫描
达到发现异常时可以在第一时间发现并处理，将安全风险降到最低的目的。
"""
# 安装方法：
# yum -y install nmap  # 安装 nmap 工具
# wget http://xael.org/norman/python/python-nmap/python-nmap-0.1.4.tar.gz
# tar -zxf python-nmap-0.1.4.tar.gz
# cd python-nmap-0.1.4
# python setup.py install

# 模块常用方法说明：
# 本章介绍python-nmap 模块的两个常用类：
# 1. PortScanner() 类：实现一个nmap 工具的端口扫描功能封装；
# 2. PortScannerHostDict() 类：实现存储与访问主机的扫描结果。

# -*- PortScanner() 类具体用法：
"""1.scan(self, host='127.0.0.1', port=None, arguments='-sV') 方法：实现指定主机、端口、nmap命令"""
# 行参数的扫描。
# host: 为字符串类型，表示扫描的主机地址，格式可以用“scanme.nmap.org”、“198.1165.0-255.1-127”表示；
# post: 为字符串类型，表示扫描的端口，可以用“22，53，110，143-4564”表示；
# arguments: 为字符串类型，表示nmap 命令行参数，格式为“-sU -sX -sC”。
# 例如：
# nm = nmap.PortScanner()
# nm.scan('192.168.1.21-22','22, 80')

"""2.command_line(self) 方法：返回的扫描方法映射到具体nmap 命令行"""
# 例如：
# >>> nm.command_line()
# u'nmap -oX - -p 22, 80 -sV 192.168.1.21-22'

"""3.scaninfo(self)方法：返回nmap扫描信息，格式为字典类型"""
# 例如：
# >>> nm.sccaninfo()
# {u'tcp': {'services': u'22, 80', 'method': u'syn'}}

"""4.all_hosts(self) 方法：返回nmap 扫描主机清单，格式为列表类型"""
# >>> nm.all_host()
# [u'192.168.1.21', u'192.168.1.22']


# -*- PortScannerHostDict() 类的一些常用方法：
"""1.hostname(self) 方法：返回扫描对象的主机名"""
# >>> nm['192;168.1.22'].hostname()
# u'SN2013-08-022'

"""2.state(self)方法：返回扫描对象的状态，包括4种状态（up、down、unknown、skipped）"""
# >>> nm['192.168.1.22'].state()
# u'up'

"""all_protocols(self)方法：返回扫描的协议"""
# >>> nm['192.168.1.22'].all_protocols()
# [u'tcp']

"""all_tcp()(self)方法：返回TCP协议扫描的端口"""
# >>> nm['192.168.1.22'].all_tcp()
# [22, 80]

"""tcp(self, port)方法：返回扫描TCP 协议port（端口）的信息"""
# >>> nm['192.168.1.22'].tcp(22)
# ['state': u'open', 'reason': u'syn-ack', 'name': u'ssh']

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