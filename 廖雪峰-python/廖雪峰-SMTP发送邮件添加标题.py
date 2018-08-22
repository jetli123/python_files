# -*- coding:utf-8 -*-
"""
    带附件的邮件可以看做包含若干部分
的邮件：文本和各个附件本身，所以，可以构造一个 MIMEMultipart 对象
代表邮件本身，然后往里面加上一个 MIMEText 作为邮件正文，再继续往
里面加上表示附件的 MIMEBase 对象即可：
"""
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = raw_input('From: ')
password = raw_input('Password: ')
to_addr = raw_input('To: ')
smtp_server = raw_input('Smtp server: ')

msg = MIMEText('hello, \r\ncui, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('python 爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候......', 'utf-8').encode()
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()