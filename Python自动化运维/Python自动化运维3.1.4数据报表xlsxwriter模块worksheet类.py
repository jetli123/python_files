# -*- coding: utf-8 -*-
"""Workbook类定义：Workbook(filename[,options])该类实现创建一个 XlsxWriter 的Workbook 对象。
Workbook 类代表整个电子表格文件，并且存储在磁盘上。
参数filename(string类型) 为创建的Excel 文件存储路径；
参数options(Dict 类型)为可选的Workbook 参数，一般作为初始化工作表内容格式，
例如值为｛'strings_to_numbers': True｝表示使用 worksheet.write() 方法激活字符串转换数字。"""
import xlsxwriter

# add_worksheet([sheetname])方法，作用是添加一个新的工作表，参数 sheetname(String 类型)为可选
# 的工作表名称，默认为Sheet1。
# 例如：
"""
# worksheet1 = workbook.add_worksheet()
# worksheet2 = workbook.add_worksheet()
# worksheet3 = workbook.add_worksheet()
"""

# add_format([properties]) 方法， 作用是在工作表中创建一个新的格式对象来格式化单元格。
# 参数： properties(dict 类型) 为指定一个格式属性的字典，例如设置加粗格式对象，
# workbook.add_format({'bold': True}) 。
# 等价的设置加粗格式代码：
"""
bold = workbook.add_format()
bold.set_bold()
"""

# add_char(options选择项)方法：作用是在工作表中创建一个图表对象，内部是通过insert_char() 方法
# 来实现了，参数 options(dict 类型) 为图表指定一个字典属性，
# 例如：设置一个线条类型的图表对象，
"""
chart = workbook.add_char({'type': 'line'})。
"""

# close() 方法： 作用是关闭工作表文件，例如：
"""
workbook.close()
"""

""""""""""""
# -*- Worksheet 类
# write(row, col, *args) 方法，作用：写普通数据到工作表的单元格，
# row 为行坐标，
# col 为列坐标，坐标索引起始值为0；
# *args 可变参数 为数据内容，可以为数字公式、字符串或格式对象。
# 为简化不同数据类型的写入过程，write 方法简化为具体数据类型方法的别名，
# 包括：http://www.etju.com/
# 1.write_string() 写入字符串类型数据，如：
"""  worksheet.write_string(0, 0, 'Your text here')"""

# 2.write_number() 写入数字类型数据，如：
"""  worksheet.write_number('A2', 2.33422)"""

# 3. write_blank() 写入空类型数据，如：
"""  worksheet.write_blank('A2', None)"""

# 4.write_formula() 写入公式类型数据，如：
""" worksheet.write_formula(2, 0, '=SUM(B1:B5)')"""

# 5.write_datetime() 写入日期类型数据，如：
"""
worksheet.write_datetime(7, 0,datetime.datetime.strptime('2013-01-23', '%Y-%m-%d'), workbook.add_format(
 {'num_format': 'yyyy-mm-dd'}))"""

# 6.write_boolean() 写入逻辑类型数据，如：
"""  worksheet.write_boolean(0, 0, True)"""

# 7.write_url()  写入超链接类型数据，如：
""" worksheet.write_url('A1', 'ftp://www.python.org')"""

# 8.set_row(row, height, cell_format, options)方法,作用是设置行单元格的属性，
# row(int 类型) 指定行位置，起始下标为0；
# height(float 类型) 设置行高，单位像素
# cell_format(format 类型) 指定格式对象
# options(dict类型) 设置行 hidden(隐藏)、level（组合分级）、collapsed（折叠）
"""
worksheet.write('A1', 'hello') # 在A1 单元格写入‘Hello'字符串
cell_format = workbook.add_format({'bold': True}) # 定义一个加粗的格式对象
worksheet.set_row(0, 40, cell_format)  # 设置第一行单元格高度为40像素，且引用加粗格式对象
worksheet.set_row(1, None, None, {'hidden': True})  # 隐藏第2 行单元格
"""

# 9.set_column(first_col, last_col, width, cell_format, options)方法，作用：
# 为设置一列或多列单元格属性。
# first_col(int 类型) 指定开始列位置，起始下标为0；
# last_col(int 类型) 指定结束位置，起始下标为0，可以设置成与first_col一样
# width(float 类型) 设置列宽，
# cell_format(Format 类型) 指定格式对象；
# options(dict 类型) 设置行 hidden（隐藏）、level(组合分级)、collapsed（折叠）。
# 实例：
"""
worksheet.write('A1', 'Hello') # 在A1 单元格写入 'Hello'字符串
worksheet.write('B1', 'World') # 在B1 单元格写入 字符串
cell_format = workbook.add_format({'bold': True})
worksheet.set_column(0,1, 10,cell_format) # 定义一个加粗的格式对象设置0到1即（A到B）
                                          # 列单元格宽度为10 像素，且引用加粗格式对象
worksheet.set_column('C:D', 20) # 设置C到D 列单元格宽度为20 像素
worksheet.set_column('E:G', None, None, {'hidden': 1})  # 隐藏E到G列单元格
"""

# 10.insert_image(row, col, image[. options]) 方法，作用：是插入图片到指定单元格，
# 支持PNG、JPEG、BMP等图片格式。
# row: 为行坐标；
# col: 为列坐标，坐标索引起始值为0；
# image(string 类型) 为图片路径；
# options(dict 类型) 为可选参数，作用指定图片位置、比例、链接URL 等信息。
# 例如：
"""
worksheet.insert_image('B5', 'img/python-logo.png', {'url': 'http://python.org'})
"""


workbook = xlsxwriter.Workbook('C:/Users/JETLi/Desktop/demo2.xlsx')
worksheet1 = workbook.add_worksheet()
worksheet2 = workbook.add_worksheet('Foglio2')
worksheet3 = workbook.add_worksheet(u'地区成绩')
worksheet4 = workbook.add_worksheet('Data')

worksheet1.set_column('A:A', 10)
worksheet1.set_column('B:B', 45)
worksheet2.set_column('B:B', 10)
worksheet2.set_column('C:C', 20)
worksheet3.set_column('D:D', 110)
worksheet4.set_column('E:E', 28)
worksheet4.set_column('A:A', 20)

# bold = workbook.add_format({'bold': True})
bold = workbook.add_format()
bold.set_bold()
worksheet1.write_string('A1', 'NAME', bold)
worksheet1.write_string('B1', 'Address', bold)
worksheet1.write_string('A2', 'Jetli')
worksheet1.write_string('B2', u'美国华盛顿州加利福尼斯区康宁丽纶路2221号')
worksheet1.write_number(2, 0, 100)
worksheet1.write_number(3, 0, 322)
worksheet1.write_formula(4, 0, '=SUM(A3:A4)')

worksheet2.write('A1', 'UserName', bold)
worksheet2.write('B1', 'String', bold)
worksheet2.write(1, 0, 'Arhel')
worksheet2.write(1, 1, u'他来自美丽的星球，杰尔马伽马星系')
worksheet2.insert_image('C6', r'C:\Users\JetLi\Desktop\222.png')
worksheet2.insert_image('C32', r'C:\Users\JetLi\Desktop\2333.png')

worksheet3.write_string('A1', 'ID', bold)
worksheet3.write_string('C1', 'Ne_Name', bold)
worksheet3.write_number(1, 0, 203, bold)
worksheet3.write_number(2, 0, 2934)
worksheet3.write_blank('B4', None)
worksheet3.write_formula(3, 0, '=SUM(A2:A3)')
worksheet3.write_string(1, 2, 'hss201bnk')
worksheet3.write_string(2, 2, 'hssco103-alias')
worksheet3.insert_image('D6', r'C:\Users\JetLi\Desktop\yuzhou.png')

worksheet4.write_string('A1', 'URL', bold)
worksheet4.write_string('B1', 'Introductions', bold)
worksheet4.write_url('A2', 'ftp://www.python.org')
worksheet4.write_string(1, 2, u'Python网址')
cell_format = workbook.add_format({'bold': True})
worksheet4.set_row(0, 40, cell_format)
worksheet4.set_row(2, None, None, {'hidden': True})
worksheet4.set_column('A:B', 30)
worksheet4.set_column(2, 4, 40, cell_format)
worksheet4.set_column('F:I', None, None, {'hidden': True})
worksheet4.insert_image('D10', r'C:/Users/JetLi/Desktop/python.png', {'url': 'http://www.python.org'})
workbook.close()
