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
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入 Email 地址和口令:
from_addr = raw_input('From: ')
password = raw_input('Password: ')
to_addr = raw_input('To: ')  # 输入收件人地址:
smtp_server = raw_input('Smtp server: ')  # 输入 SMTP 服务器地址:
# smtp_server = 'smtp.qq.com'
# 邮件对象:
msg = MIMEMultipart()
msg['From'] = _format_addr('<%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候......', 'utf-8').encode()

# 邮件正文是MIMEText:
'''msg.attach(MIMEText('Hello, \r\nCui, send to Python...\r\n'
                    'Oh, My god!\r\nPlease look up picture.', 'plain', 'utf-8'))
'''

"""把一个图片嵌入到邮件正文中"""
msg.attach(MIMEText('<html><body><h1>Hello, Cui, send to Python...'
                    'Oh, My god! Please look up picture.</h1>' + '<p><img src="cid:0"></p>' +
                    '</body></html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('D:\Python software\python file\oooooo.png', 'rb') as f:
    # 设置附件的 MIME 和文件名，这里是 png 类型:
    mime = MIMEBase('image', 'png', filename='oooooo.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='oooooo.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用 Base64 编码:
    encoders.encode_base64(mime)
    # 添加到 MIMEMultipart:
    msg.attach(mime)

"""安全地发送邮件，可以加密 SMTP 会
话，实际上就是先创建 SSL 安全连接，然后再使用 SMTP 协议发送邮
件。"""
# smtp_port = 465  # SSl 连接端口号
smtp_port = 25  # SMTP默认端口号
server = smtplib.SMTP(smtp_server, smtp_port)
# server.starttls()  # 创建 SSL 安全连接
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

""""小结：
  使用 Python 的 smtplib 发送邮件十分简单，只要掌握了各种邮件类型的
构造方法，正确设置好邮件头，就可以顺利发出。
构造一个邮件对象就是一个 Messag 对象，如果构造一个 MIMEText 对象，
就表示一个文本邮件对象，如果构造一个 MIMEImage 对象，就表示一个
作为附件的图片，要把多个对象组合起来，就用 MIMEMultipart 对象，而
MIMEBase 可以表示任何对象。它们的继承关系如下：

Message
+- MIMEBase
    +- MIMEMultipart
    +- MIMENonMultipart
        +- MIMEMessage
        +- MIMEText
        +- MIMEImage
"""