# -*- coding:utf-8 -*-
"""构造一个最简单的纯文本邮件："""
from email.mime.text import MIMEText

# 造 MIMEText 对象时，第一个参数就是邮件正文，第二个参数是
# MIME 的 subtype，传入'plain'表示纯文本，最终的 MIME 就是
# 'text/plain'，最后一定要用 utf-8 编码保证多语言兼容性。
msg = MIMEText('Hello', 'plain', 'utf-8')

"""然后，通过 SMTP 发出去："""
#  输入 Email 地址和口令:
from_addr = raw_input('From: ')
password = raw_input('Password: ')
# 输入收件人地址:
to_addr = raw_input('To: ')
# to_addr2 = raw_input('To2: ')
# 输入 SMTP 服务器地址:
smtp_server = raw_input('SMTP server: ')
import smtplib

server = smtplib.SMTP(smtp_server, 25)  # SMTP 协议默认端口是 25
server.set_debuglevel(1)  # set_debuglevel(1)就可以打印出和 SMTP 服务器交互的所有信息
server.login(from_addr, password)  # login()方法用来登录 SMTP服务器
# sendmail()方法就是发邮件，由于可以一次发给多个人，所以
# 传入一个 list，邮件正文是一个 str，as_string()把 MIMEText 对象变成str。
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()