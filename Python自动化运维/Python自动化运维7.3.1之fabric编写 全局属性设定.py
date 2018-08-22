# -*- coding: utf-8 -*-
"""env 对象的作用是定义fabfile 的全局设定，支持多个属性，包括目标主机、用户名、密码、角色等，
各属性说明如下："""

# env.host，定义目标主机，可以用IP 或主机名表示，以Python 的列表形式定义，如 env.hosts=['192.168.1.1',192.168.1.2'].
# env.exclude_hosts，排除指定主机，如 env.exclude_hosts=['192.168.1.22']
# env.user，定义用户名，如 env.user="root"。
# env.port，定义目标主机端口，默认为22，如 env.port="22"
# env.password，定义密码，如 env.password='admin@123'
# env.passwords，与password 功能一样，区别在于不同主机不同密码的应用场景，需要注意的是，配置passwords时 需配置
#               用户、主机、端口等信息，如：env.passwords = {
#                                               'root@192.168.1.1:22': 'admin@123',
#                                               'root@192.168.1.1:23': 'admin@456',
#                                               'root@192.168.1.1:24': 'admin@789',

# env.gateway，定义网关（中转、堡垒机）IP，如 env.gateway = '192.168.1.22'。
# env.deploy_release_dir，自定义全局变量，格式：env.+ "变量名称"，如 env.deploy_release_dir、env.age、env.sex 等。
# env.roledefs，定义角色分组，比如 web 组与db 组 主机区分开来，定义如下：
#       env.passwords = {
#           'webservers': ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4']
#           'dbservers': ['192.168.1.5', '192.168.1.6']

# 引用时使用Python 修饰符的形式进行，角色修饰符下面的任何函数为其作用域，下如图。
"""
@roles(webservers')
def web('kbservers')
    run('/etc/init.d/nginx start')

@roles('dbservers')
def dbtask():
    run('/etc/init.d/mysql start')

@roles('webservers', 'dbservers')
def pubclitask():
    run('uptime')

def deploy():
    execute(webtask)
    execute(dbtask)
    execute(pubclitask)

在命令行执行 # fab deploy 就可以实现不同角色执行不同的任务 函数了
"""

# 常用API
# Fabric 提供了一组简单但功能强大的 fabric.api 命令集，简单地调用这些API 就能完成大部分应用场景需求。
# Fabric 支持常用的方法及说明如下：
# local，执行本地命令，如：local('uname -s')
# lcd，切换本地目录，如：lcd('/home')
# cd，切换远程目录，如：cd('/data/logs')
# run，执行远程命令，如：run('free -m')
# sudo，sudo 方式执行远程命令，如：sudo('/etc/init.d/httpd start')
# put，上传本地文件到远程主机，如：put('/home/user.info', '/data/user.info')
# get，从远程主机下载文件到本地，如：get('/data/user.info', '/home/root.info')
# prompt，获得用户输入信息，如：prompt('please input user password:')
# confirm，获得提示信息确认，如：confirm("Tests failed.Continue[Y/N]?")
# reboot，重启远程主机，如：reboot()
# @task，函数修饰符，标识的函数为 fab 可调用的，非标记对 fab 不可见，纯业务逻辑；
# @runs_once，函数修饰符，标识的函数只会执行一次，不受多台主机影响。
