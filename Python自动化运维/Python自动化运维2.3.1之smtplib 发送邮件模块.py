# -*- coding: utf-8 -*-
"""smtplib 模块的常用类与方法"""

# -*- SMTP类定义：
# smtplib.SMTP([host[,post[,local_hostname[,timeout]]]])
# host参数为远程smtp主机地址，比如smtp.163.com；
# port 为连接端口，默认为25；
# local_hostname的作用是在本地主机FQDN（完整的域名）发送HELO/EHLO（标识用户身份）指令；
# timeout为连接或尝试在多少秒超时。

# -*- SMTP 类的方法如下：
# -1)
"""SMTP.connect([hos[port]]) 方法，连接远程smtp主机方法，host 为远程主机地址，
port 为远程主机smtp端口，默认为25， 也可以直接使用host:port 形式来表示，
例如：SMTP.connect("smtp.163.com", "25")。"""

# -2)
"""SMTP.login(user, password) 方法，远程主机的校验方法，参数为用户名与密码，
如：SMTP.login("python_2014@163.com", "sdjkg358")。"""

# -3)
"""SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options]) 方法，
实现邮件的发送功能，参数依次为 发件人、收件人、邮件内容，
例如：SMTP.sendmail("python2014@163.com", "demo@domail.com", body),
其中 body　内容定义如下："""

# """From: python2014@163.com
# To: demo@domail.com
# subject: test mail

# test mail body"""

# -4)
"""SMTP.starttls([keyfile[, certfile]]) 方法， 启用 TLS（安全传输）模式，所有
SMTP指令都将加密传输，例如使用gmail 的smtp服务时需要启动此项才能正常发送邮件，
如：SMTP.starttls()。"""

# -5)
"""SMTP.quit() 方法，断开smtp 服务器的连接。"""

import smtplib
import string

HOST = "smtp.163.com"  # 定义 smtp 主机
SUBJECT = "明天上班"  # 定义邮件主题
TO = "Jet_Oracle@outlook.com"  # 定义收邮件人
FROM = "llj_0824@163.com"  # 定义发邮件人
text = "Python rules them all!"  # 邮件内容
BODY = string.join((  # 组装sendmail方法的邮件主题内容， 各段以"\r\n" 进行分隔
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT,
        "",
        text
        ), "\r\n")
server = smtplib.SMTP()  # 创建一个SMTP对象
server.connect(HOST, "25")  # 通过connect方法连接smtp 主机
server.starttls()  # 启动安全传输模式
server.set_debuglevel(1)
server.login("llj_0824@163.com", "abc")
server.sendmail(FROM, [TO], BODY)  # 邮件发送
server.quit()  # 断开smtp连接