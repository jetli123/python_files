# -*- coding: utf-8 -*-
"""通过MIMEText 类来实现HTML 格式的邮件，
当要求包含图片数据的邮件内容时，需要引用MIMEImage 类，
若邮件主题由多个MIME对象组成，则同时需引用MIMEMultipart 类进行组装。"""

# 示例：通过MIMEText 与 MIMEImage 类的组合来实现图文格式的服务器性能报表邮件定制
import smtplib
from email.mime.text import MIMEText  # 导入MIMEMultipart 类
from email.mime.multipart import MIMEMultipart  # 导入 MIMEText 类
from email.mime.image import MIMEImage  # 导入 MIMEImage 类

HOST = "smtp.163.com"  # 定义 smtp主机
SUBJECT = u"业务性能数据报表"  # 定义邮件标题
FROM = "llj_0824@163.com"  # 定义邮件发件人
TO = "cuiak@ihotsoft.com"  # 定义邮件收件人


def adding(src, imgid):  # 添加图片函数， 参数1：图片路径， 参数2：图片 id
    fp = open(src, 'rb')  # 打开图片文件
    msgImage = MIMEImage(fp.read())  # 创建MIMEImage 对象， 读取图片内容并作为参数
    fp.close()  # 关闭文件
    msgImage.add_header('Content-ID', imgid)  # 指定图片文件的Content-ID, <img>标签 src 用到

    return msgImage  # 返回邮件对象

msg = MIMEMultipart('related')  # 创建MIMEMultipart 对象，采用 related 定义内嵌资源的邮件体
msgtext = MIMEText("""  # 创建一个MIMEText对象，HTML 元素包括表格<table>及图片<img>
    <table width="600" border="0" cellspacing="0" cellpadding="4">
        <tr bgcolor="#CECFAD" height="20" style="font-zise:14px">
            <td colspan=2>* 官网性能数据 <a href="www.ifeng.com">更多>></a>
            </td>
        </tr>
        <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
            <td>
                <img src="cid:io"></td><td>
                <img src="cid:key_hit"></td>
        </tr>
        <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
            <td>
                <img src="cid:mem"></td><td>
                <img src="cid:swap"></td>
        </tr>
    </table>
""", "html", "utf-8")  # <img>标签的src 属性是通过Content-ID 来引用的

# MIMEMultipart 对象附加MIMEText的内容
msg.attach(msgtext)
# 使用MIMEMultipart 对象附加 MIMEImage 的内容
msg.attach(adding("G:/Python27/img/bytes_io.png", "io"))
msg.attach(adding("G:/Python27/img/os_mem.png", "mem"))
msg.attach(adding("G:/Python27/img/myisam_key_hit.png", "key_hit"))
msg.attach(adding("G:/Python27/img/os_swap.png", "swap"))
msg['Subject'] = SUBJECT  # 邮件标题
msg['From'] = FROM  # 邮件发件人
msg['To'] = TO  # 邮件收件人
try:
    server = smtplib.SMTP()
    server.connect(HOST, "25")
    server.starttls()
    server.login(FROM, "123233")
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print "发送成功！"
except Exception as e:
    print "失败："+str(e)