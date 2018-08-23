# -*- coding: utf-8 -*-
"""email to report"""

# 本示例通过MIMEText 与 MIMEImage 类的组合，实现图文邮件格式
# 另，在通过 MIMEText 类再定义 Content-Disposition 属性来实现带附件的邮件
import smtplib
from email.mime.text import MIMEText  # 导入 MIMEText 类
from email.mime.image import MIMEImage  # 导入 MIMEImage 类
from email.mime.multipart import MIMEMultipart  # 导入 MIMEMultipart 类

HOST = 'smtp.163.com'  # 定义 smtp 主机
SUBJECT = u'官网业务服务指令周报'  # 定义邮件主题
TO = 'cuiak@ihotsoft.com'  # 定义邮件收件人'
FROM = 'llj_0824@163.com'  # 定义邮件发件人


def addimg(src, imgid):  # 添加图片函数， src:图片路径，imgid:图片id
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())  # 创建MIMEImage对象，读取图片内容作为参数
    fp.close()
    # 指定图片文件的 Content-ID, <img>标签src 用到
    msgImage.add_header('Content-ID', imgid)
    return msgImage

# 创建MIMEMultipart 对象，采用related 定义内嵌资源的邮件体
msg = MIMEMultipart('related')
# 创建一个MIMEText 对象，HTML 元素包括文字与图片<img>
msgtext = MIMEText("<font color=red>官网业务周平均延时表：<br><img src=\"cid:weekly\"\
                   border=\"1\"><br>详细内容见附件。</font>", "html", "utf-8")
# MIMEMultipart 对象附加MIMEText 的内容
msg.attach(msgtext)
# 使用 MIMEMultipart 对象附加 MIMEImage 的内容
msg.attach(addimg("G:/Python27/img/weekly.png", "weekly"))
# 创建一个MIMEText 对象，附加 week_report.xlsx 文档
attach = MIMEText(open("G:/Python27/img/week_report.xlsx", "rb").read(), "base64", "utf-8")
# 指定文件格式类型
attach["Content-Type"] = "application/octet-stream"
# 指定Content-Disposition 值为attachment 则出现下载保存对话框，保存的默认文件名使用 filename 指定
# 由于qqmial 使用 gb18030 页面编码， 保证文件名不出现乱码，对文件名进行编码转换
attach["Content-Disposition"] = \
    "attachment; filename=\"业务服务质量周报.xlsx\"".decode("utf-8").encode("gb18030")  # gb18030
msg.attach(attach)  # MIMEMultipart 对象附加 MIMEText 附件内容

msg['Subject'] = SUBJECT  # 邮件主题
msg['From'] = FROM  # 邮件发件人，邮件头部可见
msg['To'] = TO  # 邮件收件人，邮件头部可见
try:
    server = smtplib.SMTP()
    server.connect(HOST, "25")
    server.starttls()  # 启动安全传输模式
    server.login(FROM, "password to you")
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print("邮件发送成功！")
except Exception as e:
    print("失败"+str(e))
