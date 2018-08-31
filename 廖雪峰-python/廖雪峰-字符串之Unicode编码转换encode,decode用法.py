# -*- coding: utf-8 -*-

# 用记事本编辑的时候，从文件读取的 UTF-8 字符被转换为 Unicode 字符
# 到内存里，编辑完成后，保存的时候再把 Unicode 转换为 UTF-8 保存到
# 文件：

# 浏览网页的时候，服务器会把动态生成的 Unicode 内容转换为 UTF-8 再传输到浏览器

# 在最新的 Python 3 版本中，字符串是以 Unicode 编码的，也就是说，Python 的字符串支持多语言
# 对于单个字符的编码，Python 提供了 ord()函数获取字符的整数表示，
# chr()函数把编码转换为对应的字符

print(ord('A'))
print(ord('C'))
print(ord('中'))  # 20013
print(ord('文'))  # 25991

print(chr(20013))  # 中
print(chr(25991))  # 文

# 一、将str 转换为 bytes

# 由于 Python 的字符串类型是 str，在内存中以 Unicode 表示，一个字符
# 对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把
# str 变为以字节为单位的 bytes。

# Python 对 bytes 类型的数据用带 b 前缀的单引号或双引号表示:
x = b'ABC'

# 以 Unicode 表示的 str 通过 encode()方法可以编码为指定的 bytes，例如:
print('str转换为字节流：', 'ABC'.encode('ascii'))  # b'ABC'
print('中文转换为字节流：', '中文'.encode('utf-8'))  # b'\xe4\xb8\xad\xe6\x96\x87'
# 总结：
# 1.纯英文的 str 可以用 ASCII 编码为 bytes，内容是一样的；
# 2.含有中文的 str 可以用 UTF-8 编码为 bytes。
# 含有中文的 str 无法用 ASCII 编码，因为中文编码的范围超过了 ASCII 编码的范围，Python 会报错

# 二、读取字节流，bytes 转为 str
# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把 bytes 变为 str，就需要用 decode()方法：
print('字节流转换为str:', b'ABC'.decode('ascii'))
print('中文字节流转换为str：', b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))



a = open(r'G:\PyCharm\python3_test\123', encoding='utf-8')  # 读取文件获得的字节流 bytes
for i in a.readline():
    u_str = ord(i)  # 获取中文字符串整数表示
    print(u_str, ":", chr(u_str))  # 将整数表示的中文编码转换成中文字符串
a.close()