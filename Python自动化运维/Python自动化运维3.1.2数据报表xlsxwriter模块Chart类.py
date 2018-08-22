# -*- coding: utf-8 -*-
"""Chart 类实现在 XlsxWriter 模块中图表组件的基类，支持的图表类型包括面积、
条形图、柱形图、折线图、饼图、散点图、股票和雷达等，一个图表对象是通过Workbook(工作簿)的
add_chart 方法创建，通过{tpye, '图表类型'} 字典参数指定图表的类型。
语句如下："""
import xlsxwriter


# """
# chart = workbook.add_chart({'type': 'column'}) # 创建一个column(柱形) 图表
# """
# -*- 图表类型说明：
# area: 创建一个面积样式的图表
# bar: 创建一个条形样式的图标
# column: 创建一个柱形样式的图表
# line: 创建一个线性样式的图表
# pie: 创建一个饼图样式的图表
# scatter: 创建一个散点样式的图表
# stock: 创建一个股票样式的图表
# radar: 创建一个雷达样式的图表

# 在通过insert_chart() 方法插入到指定位置：
# """
# worksheet.insert_chart('A7', chart) # 在A7单元格插入图表
# """
# chart 类常用的方法：
# 1.chart.add_series(options) 方法：作用为添加一个数据系列到图表
# 参数：options(dict 类型) 设置图表系列选项的字典，如下：
# """
# chart.add_series({
#     'categories': '=Sheet1!$A$1:$A$5',
#     'values':     '=Sheet1!$B$1:$B$5',
#     'line':       {'color': 'red'},
# })"""
# 参数：categories 是设置图表类别标签范围
# 参数：values 为设置图表数据范围
# 参数：line 为设置图表线条属性，包括宽度

# 其他常用方法：
# 1.chart.set_x_axis(options) 方法：设置图表 X 轴选项，如下：
# """
# chart.set_x_axis({
#     'name': 'Earnings per Quarter'， # 设置 X 轴标题名称
#     'name_font': {'size': 14, 'bold': True}, # 设置 X 轴标题字体属性
#     'num_font': {'italic': True}, # 设置 X 轴数字字体属性
# })"""

# 2.chart.set_size(options) 方法： 设置图表大小，如：chart.set_size({'width': 720, 'height': 576}),
# width 为宽度， height 为高度。

# 3.chart.set_title(options) 方法：设置图表标题，如：chart.set_title({'name': 'Year End Results'})

# 4.chart.set_style(style_id) 方法：设置图表样式，style_id 为不同数字则代表不同样式，如：chart.set_style(37)

# 5.chart.set_table(options) 方法：设置 X 轴为数据表格形式，如：chart.set_table().

# 6.chart.set_y_axis(options)方法：设置y 轴（左侧）小标题 chart.set_y_axis({'name': 'Mb/s'})  #
""""""""""""  """"""""""""
workboob = xlsxwriter.Workbook('C:/Users/JetLi/Desktop/abc.xlsx')
worksheet = workboob.add_worksheet('weeks')

cell_format = workboob.add_format({'bold': True})
worksheet.set_row(0, 25, cell_format)
worksheet.set_row(1, 25, cell_format)
worksheet.set_column('A:C', 20)
worksheet.set_column(3, 4, 10, cell_format)
worksheet.write_string('A1', 'USER', cell_format)
worksheet.write_string('B1', 'INT', cell_format)
worksheet.write_string(1, 0, u'粒度')
worksheet.write_url(2, 0, 'http://www.etju.com/')
worksheet.write_url('A4', 'http://www.baidu.com/')
worksheet.write_number(1, 1, 1000)
worksheet.write_number(2, 1, 2000)
worksheet.write_formula(3, 1, '=SUM(B2:B3)')
worksheet.insert_image('E15', r'C:/Users/JetLi/Desktop/yuzhou.png', {'url': 'http://www.etju.com/'})
chart = workboob.add_chart({'type': 'column'})
chart.add_series({
    'categories': '=weeks!$A$7:$A$15',
    'values':     '=weeks!$B$7:$B$15',
    'line':       {'color': 'red'},
})
chart.set_x_axis({
    'name': 'Earnings per Quarter',
    'name_font': {'size': 14, 'bold': True},
    'num_font': {'italic': True},
})
chart.set_title({'name': 'Year End Results'})
chart.set_style(37)
worksheet.insert_chart('A16', chart)
workboob.close()