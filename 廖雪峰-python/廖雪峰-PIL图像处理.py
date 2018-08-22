# -*- coding:utf-8 -*-
__author__ = 'JetLi'
__version__ = '1.2_low_3'
__history__ = '2018/03/29'

from PIL import Image, ImageFilter

"""来看看最常见的图像缩放操作，只需三四行代码："""
im = Image.open('G:\\PyCharm\\untitled\\photo1.jpg')  # 打开一个 jpg 图像文件，注意是当前路径:
w, h = im.size  # 获得图像尺寸:
print('Original image size: %sx%s' % (w, h))
# im.thumbnail((w//2, h//3))  # 缩放到 50%:
# print('Resize image to: %sx%s' % (w//2, h//3))
# im.save('thumbnail5.jpg', 'png')  # 把缩放后的图像用 jpeg 格式保存:

"""模糊效果也只需几行代码："""

im1 = Image.open('G:\\PyCharm\\untitled\\thumbnail5.jpg')
# 应用模糊滤镜:
im2 = im1.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'png')