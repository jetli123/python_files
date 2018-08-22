# -*- coding: utf-8 -*-
"""send mail for url"""
__author__ = 'JetLi'
__history__ = '2018/4/10'

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
import smtplib
import re
import pprint
import json
from urllib import urlopen


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


class Email(object):

    def __init__(self, from_addr, password, to_addr, smtp_server):
        self.from_addr = from_addr
        self.password = password
        self.to_addr = to_addr
        self.smtp_server = smtp_server

    def to_mail(self):
        msg = MIMEMultipart()
        msg['From'] = _format_addr('来自阿斯塔纳的Python爱好者<%s>' % self.from_addr)
        msg['To'] = _format_addr('Python 领导者<%s>' % self.password)
        msg['Subject'] = Header('共享sina 相关的URL', 'utf-8').encode()
        msg.attach(MIMEText('Hello,\r\nLook at this txt.', 'plain', 'utf-8'))

        with open(r'D:/Python27/python file/abc.txt') as o:
            mime = MIMEBase('text', 'txt', filename='abc.txt')
            mime.add_header('Content-Disposition', 'attachment', filename='abc.txt')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            mime.set_payload(o.read())
            msg.attach(mime)

        server = smtplib.SMTP(self.smtp_server, 25)
        server.set_debuglevel(1)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [self.to_addr], msg.as_string())
        server.quit()

if __name__ == '__main__':

    ac = urlopen(r'http://www.ifeng.com')
    with open(r'D:/Python27/python file/jet.txt', 'w')as f:
        f.write(ac.read())

    with open(r'D:/Python27/python file/jet.txt') as e:
        a = re.compile(r'.*?<a href="(http.*?)".*?</a>.*')
        c = []
        for line in e.readlines():
            line = line.strip()
            b = a.match(line)
            if b:
                c.append(b.groups())
        pprint.pprint(c)
    with open(r'D:/Python27/python file/abc.txt', 'w') as f:
        f.write(json.dumps(c))

    #
    # pprint.pprint(c)
    # from_addr = raw_input("From: ")
    # password = raw_input("Password: ")
    # to_addr = raw_input("To: ")
    # smtp_server = raw_input("SMTP_Server: ")
    obd = Email('llj_0824@163.com', 'lilianjie1988', 'Jet_Oracle@outlook.com', 'smtp.163.com')
    obd.to_mail()
