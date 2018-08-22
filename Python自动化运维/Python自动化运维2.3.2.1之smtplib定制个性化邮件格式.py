# -*- coding: utf-8 -*-
"""我们经常会制定业务质量报表，在邮件主题中会包含HTML、图像、声音以及附件格式等，
MIME 作为一种新的扩展邮件格式很好地补充了这一点"""

""" email.mime.multipart.MIMEMultipart([_subtype[,boundary[,_subpart[,_params]]]]"""
# 作用是生成包含多个部分的邮件的MIME 对象，参数_subpart指定要添加到
# "Content-type:multipart/subtype" 报头的可选的三种子类型，分别为mixed、related、alternative,
# 1.默认值为mixed。定义mixed实现构建一个带附件的邮件体；
# 2.定义related实现构建内嵌资源的邮件体；
# 3.定义alternative 则实现构建纯文本与超文本共存的邮件体。

"""email.mime.image.MIMEAudio(_audiodata[,_subtype[,_encoder[,**_params]]])"""
# 创建包含音频数据的邮件体，_audiodata包含原始二进制音频数据的字节字符串。

"""email.mime.image.MIMEImage(_imagedata[,_subtpye[,_encoder[,**_params]]])"""
# 创建包含图片数据的邮件体，_imagedata是包含原始图片数据的字节字符串。

"""email.mime.text.MIMEText(_text[,_subtype[,_charset]])"""
# 创建包含文本数据的邮件体，_text 是包含消息负载的字符串，_subtype指定文本类型，
# 支持plain（默认值）或 html 类型的字符串。
