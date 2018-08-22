# -*- coding: utf-8 -*-
"""Python 操作Excel 模块 XlsxWriter, 可以操作多个工作表的文字、
数字、公式、图标等"""
# XlsxWriter 模块具有以下功能：
# 1.兼容Excel xlsx文件，支持Excel2003 、Excel2007 等版本。
# 2.支持所有Excel 单元数据格式
# 3.单元格合并、批注、自动筛选、丰富多格式字符串等
# 4.支持工作表PNG、JPEG 图像，自定义图标
# 5.内存优化模式支持写入大文件

# 安装方法：
# pip install XlsxWriter   pip安装方法
# easy_install XlsxWriter  easy_install 安装方法
# 源码安装方法：
# curl -O -L http://github.com/jmcnamara/XlsxWriter/archive/master.tar.gz
# tar zxvf master.tar.gz
# cd XlsxWriter-master/
# python setup.py install

# 示例：
# 实现插入文字（中英字符）、数字（求和计算）、图片、单元格格式
import xlsxwriter

workbook = xlsxwriter.Workbook('C:/Users/JETLi/Desktop/demol.xlsx')  # 创建一个Excel文件
worksheet = workbook.add_worksheet()  # 创建一个工作表

worksheet.set_column('A:A', 20)  # 设定第一列（A）宽度为20 像素
bold = workbook.add_format({'bold': True})  # 定义一个加粗的格式对象

worksheet.write('A1', 'Hello')  # A1 单元格写入 'Hello'
worksheet.write('A2', 'World', bold)  # A2 单元格写入'World' 并引用加粗格式对象bold
worksheet.write('B2', u'中文测试', bold)  # B2单元格写入中文并引用加粗格式对象 bold

worksheet.write(2, 0, 32)  # 用行列表示法写入数字 '32'与'35.5'
worksheet.write(3, 0, 35.5)  # 行列表示法的单元格下标以0作为起始值，'3, 0' 等价于'A4'
worksheet.write(4, 0, '=SUM(A3:A4)')  # 求 A3:A4 的和，并将结果写入 '4, 0'，即 'A5'
worksheet.write(5, 0, 100)

worksheet.insert_image('B5', r'C:\Users\JetLi\Desktop\20180516124256.png')  # 在B5 单元格插入图片
workbook.close()  # 关闭Excel 文件
