#!//usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib2
import argparse

from urllib2 import URLError

reload(sys)
sys.setdefaultencoding('utf-8')

try:
    import json
except ImportError:
    import simplejson as json


class Zabbix_api(object):
    
    def __init__(self):
        self.url = 'http://10.0.6.124:80/zabbix/api_jsonrpc.php'
        self.header = {"Content-Type": "application/json-rpc"}

    def user_login(self):
        data = json.dumps({
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": "Admin",
                "password": "zabbix"
            },
            "id": 1
            #"auth": null
        })

        request = urllib2.Request(self.url, data)
        
        for key in self.header:
            request.add_header(key, self.header[key])
        
        try:
            result = urllib2.urlopen(request)
        except URLError, e:
            print "\033[041m auth error: check RUL! \033[0m", e.code
        except KeyError, e:
            print "\033[041m auth error: check user and password ! \033[0m", e
        else:
            response = json.loads(result.read())
            result.close()
            self.authID = response['result']
            return self.authID

    def host_get(self, hostName=''): # 通过主机名 得到主机 id
        data = json.dumps({
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": "extend",
                "filter": {
                    "host": hostName
                }
            },
            "auth": self.user_login(),
            "id": 1
        })
        request = urllib2.Request(self.url, data)
        for key in self.header:
            request.add_header(key, self.header[key])

        try:
            result = urllib2.urlopen(request)
        except URLError, e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server.')
                print('Reason: ', e.reason)
            elif hasattr(e, 'code'):
                print('The server could not fulfill the request.')
                print('Error code: ', e.code)
        else:
            response = json.loads(result.read())
            # print(response)
            result.close()

            if not len(response['result']):
                print("\033[041m %s \003[0m is not exist" % hostName)
                return False

            print("主机数量: \033[31%s\033[0m" % (len(response['result'])))
            for host in response['result']:
                status = {"0": "OK", "1": "Disabled"}
                available = {"0": "Unknown", "1": "available", "2": "Unavailable"}
                if len(hostName) != 0:
                    print("HostID : %s\t HostName : %s\t HostIp : %s\t Status : %s\t Available : %s" % (host['hostid'], host['name'], self.hostid_get_hostip(hostId=host['hostid']), status[host['status']], available[host['available']]))
                    return host['hostid']



    def hostip_get(self, hostIp=''): # 通过主机IP 得到主机 id
        data = json.dumps({
            "jsonrpc": "2.0",
            "method": "hostinterface.get",
            "params": {
                "output": "extend",
                "filter": {"ip": hostIp}
            },
            "auth": self.user_login(),
            "id": 1
        })
        request = urllib2.Request(self.url, data)
        for key in self.header:
            request.add_header(key, self.header[key])

        try:
            result = urllib2.urlopen(request)
        except URLError, e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(result.read())
            # print response
            result.close()

            if not len(response['result']):
                print "\033[041m hostip \033[0m is not exist"
                return False

            print "主机数量: \33[31m%s\33[0m" % (len(response['result']))
            for hostip in response['result']:
                host = self.hostid_get_hostname(hostip['hostid'])
                if len(hostip) == 0:
                    print "HostID : %s\t HostName : %s\t HostIp : %s\t Status :\33[32m%s\33[0m \t Available :\33[31m%s\33[0m"%(hostip['hostid'],host['name'],hostip['ip'],host['status'],host['available'])
                else:
                    print "HostID : %s\t HostName : %s\t HostIp : %s\t Status :\33[32m%s\33[0m \t Available :\33[31m%s\33[0m"%(hostip['hostid'],host['name'],hostip['ip'],host['status'],host['available'])
                    return hostip['hostid']



    def hostid_get_hostname(self, hostId=''): # 通过上面两个方法得到的主机 id，获得主机名
        data = json.dumps({
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": "extend",
                "filter": {"hostid": hostId}
            },
            "auth": self.user_login(),
            "id": 1
        })
        request = urllib2.Request(self.url, data)
        for key in self.header:
            request.add_header(key, self.header[key])
        try:
            result = urllib2.urlopen(request)
        except URLError, e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(result.read())
            #print response
            result.close()

            if not len(response['result']):
                print "hostId is not exist"
                return False

            #print "主机数量: \33[31m%s\33[0m" % (len(response['result']))
            host_dict=dict()
            for host in response['result']:
                status = {"0": "OK", "1": "Disabled"}
                available = {"0": "Unknown", "1": "available", "2": "Unavailable"}
                #if len(hostId) == 0:
                #    print "HostID : %s\t HostName : %s\t Status :\33[32m%s\33[0m \t Available :\33[31m%s\33[0m" % (
                #        host['hostid'], host['name'], status[host['status']], available[host['available']])
                #else:
                #    print "HostID : %s\t HostName : %s\t Status :\33[32m%s\33[0m \t Available :\33[31m%s\33[0m" % (
                #        host['hostid'], host['name'], status[host['status']], available[host['available']])
                host_dict['name']=host['name']
                host_dict['status']=status[host['status']]
                host_dict['available']=available[host['available']]
                return host_dict



    def hostid_get_hostip(self, hostId=''): # 通过上面两个方法得到的 主机id ，获取主机IP 
        data = json.dumps({
            "jsonrpc": "2.0",
            "method": "hostinterface.get",
            "params": {
                "output": "extend",
                "filter": {"hostid": hostId}
            },
            "auth": self.user_login(),
            "id": 1
        })
        request = urllib2.Request(self.url, data)
        for key in self.header:
            request.add_header(key, self.header[key])
        try:
            result = urllib2.urlopen(request)
        except URLError, e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server could not fulfill the request.'
                print 'Error code: ', e.code
        else:
            response = json.loads(result.read())
            # print response
            result.close()

            if not len(response['result']):
                print "\033[041m hostid \033[0m is not exist"
                return False

            #print "主机数量: \33[31m%s\33[0m" % (len(response['result']))
            for hostip in response['result']:
                #print hostip
                #if len(hostip) == 0:
                #    print "HostID : %s\t HostIp : %s \t Port : %s " % (hostip['hostid'], hostip['ip'], hostip['port'])
                #else:
                #    print "HostID : %s\t HostIp :\33[32m%s\33[0m \t Port :\33[31m%s\33[0m" % (
                #        hostip['hostid'], hostip['ip'], hostip['port'])
                return hostip['ip']


    def host_delete(self,hostNames):
        hostid_list=[]
        for hostName in hostNames.split(','):
            hostid = self.host_get(hostName=hostName)
            if not hostid:
                print "主机 \033[041m %s\033[0m  删除失败 !" % hostName
                sys.exit()
            hostid_list.append(hostid)

        data=json.dumps({
                "jsonrpc": "2.0",
                "method": "host.delete",
                "params": hostid_list,
                "auth": self.user_login(),
                "id": 1
                })

        request = urllib2.Request(self.url,data)
        for key in self.header:
            request.add_header(key, self.header[key])

        try:
            result = urllib2.urlopen(request)
            result.close()
            print "主机 \033[041m %s\033[0m  已经删除 !" % hostName
        except Exception,e:
            print  e


    def template_get(self, templateName=''):
        date = json.dumps({
                "jsonrpc": "2.0",
                "method": "template.get",
                "params": {
                    "output": "extend",
                    "filter": {
                            "name": templateName
                        }   
                    },
                "auth": self.user_login(),
                "id": 1,
                 })
        request = urllib2.Request(self.url, date)
        for key in self.header:
             request.add_header(key, self.header[key])
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            print("Error as ", str(e))
        else:
            response = json.loads(result.read())
            #print response
            result.close()
            if not len(response['result']):
                print("\033[041m %s \033[0m is not exist" % templateName)
                return False
            for template in response['result']:
                if len(templateName) == 0:
                    print("template : %s \t id : %s" % (template['name'], template['templateid']))
                else:
                    self.templateID = response['result'][0]['templateid']
                    print("template Name :%s" % templateName)
                    return response['result'][0]['templateid']


    def host_link_template(self, hostName, templateName):
        hosts = []
        hostids = {}
        temp_id = self.template_get(templateName)
        #for i in hostName.split(','):
        #    hostid = self.host_get(i)
        #    hostids["hostid"] = hostid
        #    hosts.append(hostids) 
        hostid = self.host_get(hostName)
        hostids["hostid"] = hostid
        hosts.append(hostids)
        date = json.dumps({
                    "jsonrpc": "2.0",
                    "method": "host.massadd",
                    "params": {
                        "hosts": hosts,
                        "templates": temp_id      
                    },
                    "auth": self.user_login(),
                    "id": 1
                })
        request = urllib2.Request(self.url, date)
        for key in self.header:
            request.add_header(key, self.header[key])
        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            print("Error as ", str(e))
        else:
            response = json.loads(result.read())
            #print response
            result.close()
            print("主机 \033[041m %s \033[0m 关联模板 \033[041m %s \033[0m 成功 " % (hostName, templateName)) 



if __name__ == '__main__':
    zabbix = Zabbix_api()
    parser=argparse.ArgumentParser(description='zabbix api ',usage='%(prog)s [options]')
    parser.add_argument('-H','--host',nargs='?',dest='listhost',default='host',help='查询主机')
    parser.add_argument('-G','--group',nargs='?',dest='listgroup',default='group',help='查询主机组')
    parser.add_argument('-T','--template',nargs='?',dest='listtemp',default='template',help='查询模板信息')
    parser.add_argument('-A','--add-group',nargs=1,dest='addgroup',help='添加主机组')
    parser.add_argument('-C','--add-host',dest='addhost',nargs=4,metavar=('192.168.2.1', 'groupname', 'Template01,Template02', 'hostName'),help='添加主机,多个主机组或模板使用逗号')
    parser.add_argument('-d','--disable',dest='disablehost',nargs='+',metavar=('sh-aa-01'),help='禁用主机,填写主机名，多个主机名之间用逗号')
    parser.add_argument('-e','--enable',dest='enablehost',nargs=1,metavar=('sh-aa-01'),help='开启主机')
    parser.add_argument('-D','--delete',dest='deletehost',nargs='+',metavar=('sh-aa-01'),help='删除主机,多个主机之间用逗号,主机也许是IP')
    parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('-L', '--link', dest='linktemplate', nargs=2, metavar=('10.0.7.116','Template OS Linux'), help='主机关联模板')



    if len(sys.argv) == 1:
        print(parser.print_help())
        #print(zabbix.host_get(hostName='bbb'))
        #print(zabbix.hostip_get(hostIp='127.0.0.1'))
        #print(zabbix.hostid_get_hostname(hostId='10108'))
        #print(zabbix.hostid_get_hostid(hostId='10105'))
        #print(zabbix.hostgroup_get(hostgroupName='Linux servers'))
        #print(zabbix.hostgroup_get(hostgroupName='aaa'))
        #print(zabbix.host_delete('hz-aaa-02'))
        #print(zabbix.host_link_template('10.0.7.237 10.0.7.116', 'Template App MySQL'))
        # ...
    else:
        args = parser.parse_args()
        if args.listhost != 'host':
            if args.listhost:
                zabbix.host_get(args.listhost)
            else:
                zabbix.host_get()
        if args.disablehost:
            zabbix.host_disable(args.disablehost)
        if args.deletehost:
            zabbix.host_delete(args.deletehost[0])
        if args.listtemp != 'template':
            if args.listtemp:
                zabbix.template_get(args.listtemp)
            else:
                zabbix.template_get()
        if args.linktemplate != 'link':
            if args.linktemplate:
                zabbix.host_link_template(args.linktemplate[0], args.linktemplate[1])
