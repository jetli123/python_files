# -*- coding: utf-8 -*-
import xlsxwriter


workbook = xlsxwriter.Workbook('C:/Users/JETLI/Desktop/chart.xlsx')
worksheet = workbook.add_worksheet('weeks')  # 创建一个 Excel 对象
chart = workbook.add_chart({'type': 'column'})  # 创建一个图表对象
# 定义数据表头列表
title = [u'业务名称', u'星期一', u'星期二', u'星期三', u'星期四', u'星期五', u'星期六', u'星期日',
         u'平均流量']
buname = [u'业务官网', u'新闻中心', u'购物频道', u'体育频道', u'亲子频道']  # 定义频道名称
# 定义5 频道一周7天流量数据列表
data = [
    [153, 145, 158, 155, 143, 148, 154],
    [99, 89, 93, 100, 99, 92, 99],
    [201, 200, 192, 178, 200, 199, 195],
    [76, 75, 65, 69, 79, 74, 71],
    [84, 85, 88, 89, 92, 95, 87],
]
# 定义列名称和整数数值的格式对象
format1 = workbook.add_format()  # 定义 format 格式对象
format1.set_border(1)  # 定义 format 对象单元格边框加粗（1像素）的格式

# 定义行标题的格式对象
format_title = workbook.add_format()  # 定义format_title 格式对象
format_title.set_border(1)  # 定义 format_title 对象单元格边框加粗（1像素）的格式
format_title.set_bg_color('#cccccc')  # 定义format_title 对象单元格背景颜色为 '#cccccc'的格式
format_title.set_align('center')  # 定义 format_title 对象单元格居中对齐的格式
format_title.set_bold()  # 定义format_title 对象单元格内容加粗的格式

# 定义avg 平均值的格式对象
format_ave = workbook.add_format()  # 定义 format_ave 格式对象
format_ave.set_border(1)  # 定义 format_ave 对象单元格边框加粗（1像素）的格式
format_ave.set_num_format('0.00')  # 定义 format_ave 对象单元格数字类别显示格式

# 下面分别以行或列写入方式将标题、业务名称、流量数据写入起始单元格，同时引用不同格式对象
worksheet.write_row('A1', title, format_title)  # 从A1 开始的行写入标题
worksheet.write_column('A2', buname, format1)  # 从 A2 开始的列写入名称
worksheet.write_row('B2', data[0], format1)  # 从B2 开始的行写入数值data[0] 共7个数值
worksheet.write_row('B3', data[1], format1)  # 从B3 开始的行写入数值data[1] 共7个数值
worksheet.write_row('B4', data[2], format1)  # 从B4 开始的行写入数值data[2] 共7个数值
worksheet.write_row('B5', data[3], format1)  # 从B5 开始的行写入数值data[3] 共7个数值
worksheet.write_row('B6', data[4], format1)  # 从B6 开始的行写入数值data[4] 共7个数值

# 定义图标数据系列函数


def chart_series(cur_row):  # 计算（AVERAGE函数）频道周平均流量
    worksheet.write_formula('I' + cur_row, '=AVERAGE(B'+cur_row+':H'+cur_row+')', format_ave)  # I2:H2 的平均值

    chart.add_series({
        'categories': '=weeks!$B$1:$H$1',  # 将“星期一至星期日”作为图表数据标签（X轴）
        'values':      '=weeks!$B$'+cur_row+':$H$'+cur_row,  # 频道一周所有数据作为数据区域
        'line':        {'color': 'black'},  # 线条颜色定义为black 黑色
        'name':        '=weeks!$A$'+cur_row,  # 引用业务名称为图例项
    })

for row in range(2, 7):  # 数据域以第2 - 6 行进行图表数据系列函数调用
    chart_series(str(row))

# chart.set_table() 设置 X 轴表格格式，不启用
# chart.set_style() 设置图表样式，不启用
chart.set_size({'width': 577, 'height': 287})  # 设置图表大小
chart.set_title({'name': u'业务流量周报图表'})  # 设置图表上方大标题
chart.set_y_axis({'name': 'Mb/s'})  # 设置y 轴（左侧）小标题

worksheet.insert_chart('A8', chart)  # 在A8 单元格插入图表
workbook.close()  # 关闭 Excel 文档