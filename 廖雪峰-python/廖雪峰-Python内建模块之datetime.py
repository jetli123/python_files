# -*- coding: utf-8 -*-
"""
    datetime 是 Python 处理日期和时间的标准库。
"""
from datetime import datetime
import time
from datetime import timedelta

"""获取当前日期和时间"""
print '当前日期和时间:', datetime.now()
# 2018-03-20 13:44:54.672000

"""获取指定日期和时间"""
# 通过参数构造一个 datetime:
print '获取指定日期和时间:', datetime(2018, 03, 20, 14, 20, 40)
# 2018-03-20 14:20:40

"""datetime 转换为 timestamp"""
# 我们把 1970 年 1 月 1 日 00:00:00 UTC+00:00 时区的时刻称为 epoch time
# 记为 0（1970 年以前的时间 timestamp 为负数），当前时间就是相对于 epoch time 的秒数，称为 timestamp。
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
# 对应的北京时间是：
# timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
dt = datetime(2018, 03, 20, 14, 37)  # ==> datetime.datetime(2018, 3, 20, 15, 34)
timestamp = time.mktime(dt.timetuple())
print '指定日期转换为timestamp时间：', timestamp
# 1521527820.0

"""timestamp 转换为 datetime"""
# 要把 timestamp 转换为 datetime，使用 datetime 提供的 fromtimestamp()
ab = time.time()  # 1521531309.444 当前时间，新纪元开始当前的秒数
cd = time.mktime(datetime(2018, 03, 20, 15, 44).timetuple())
print '新纪元秒数转换日期：', datetime.fromtimestamp(ab).strftime("%Y-%m-%d %H:%M:%S")
# 2018-03-20 15:44:00

"""timestamp 也可以直接被转换到 UTC 标准时区的时间："""
# 格林威治标准时间
aa = time.mktime(datetime(2018, 03, 20, 15, 52).timetuple())  # 指定日期转换为秒数
print '格林威治标准时间1:', datetime.utcfromtimestamp(aa)
# 2018-03-20 07:52:00
ac = time.mktime(datetime.now().timetuple())  # 当前时间转换为秒数
print '格林威治标准时间2:', datetime.utcfromtimestamp(ac)
# 2018-03-20 07:56:45

"""str 转换为 datetime"""
# 用户输入的日期和时间是字符串，要处理日期和时间，首先必须把 str 转换为 datetime。
# 转换方法是通过 datetime.strptime()实现
print '时间字符串转换日期格式:', datetime.strptime('2018-03-20 16:20:00', '%Y-%m-%d %H:%M:%S')
# 2018-03-20 16:20:00

"""datetime 转换为 str """
# datetime.strftime() 格式化datetime 对象
ao = datetime(2018, 03, 20, 16, 15)
print ao.strftime('%a %b %d %X')
# Tue Mar 20 16:15:00

# strftime() 用来格式化datetime 对象,

# %a	星期的英文单词的缩写：如星期一， 则返回 Mon
# %A	星期的英文单词的全拼：如星期一，返回 Monday
# %b	月份的英文单词的缩写：如一月， 则返回 Jan
# %B	月份的引文单词的缩写：如一月， 则返回 January
# %c	返回datetime的字符串表示，如03/08/15 23:01:26
# %d	返回的是当前时间是当前月的第几天
# %f	微秒的表示： 范围: [0,999999]
# %H	以24小时制表示当前小时
# %I	以12小时制表示当前小时
# %j	返回 当天是当年的第几天 范围[001,366]
# %m	返回月份 范围[0,12]
# %M	返回分钟数 范围 [0,59]
# %P	返回是上午还是下午–AM or PM
# %S	返回秒数 范围 [0,61]。。。手册说明的
# %U	返回当周是当年的第几周 以周日为第一天
# %W	返回当周是当年的第几周 以周一为第一天
# %w	当天在当周的天数，范围为[0, 6]，6表示星期天
# %x	日期的字符串表示 ：03/08/15
# %X	时间的字符串表示 ：23:22:08
# %y	两个数字表示的年份 15
# %Y	四个数字表示的年份 2015
# %z	与utc时间的间隔 （如果是本地时间，返回空字符串）
# %Z	时区名称（如果是本地时间，返回空字符串）

"""datetime 加减"""
# 加减可以直接用 + 和 - 运算符，不过需要导入 timedelta 这个类
nx = datetime.now()
print nx
ox = nx + timedelta(hours=10)  # 当前时间增加 10 小时
print ox
cx = nx + timedelta(days=2)  # 当前日期增加2天
print cx
bx = nx - timedelta(minutes=60)  # 当前时间减少60 分钟
print bx
dx = nx + timedelta(days=2, hours=10)  # 当前时间增加 2天10小时
print dx

"""本地时间转换为 UTC 时间"""
ooo = datetime.utcfromtimestamp(time.mktime(datetime.now().timetuple())).strftime("%Y-%m-%d %H:%M:%S")
print '本地时间转换为 UTC 时间', ooo
