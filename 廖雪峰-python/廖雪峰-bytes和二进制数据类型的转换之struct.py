# -*- coding: utf-8 -*-
"""
    struct 模块来解决 bytes 和其他二进制数据类型的转换。
"""

"""struct 的 pack 函数把任意数据类型变成 bytes："""
import struct

print(struct.pack('>I', 10240099))
# \x00\x9c@c
# pack 的第一个参数是处理指令，
# '>I'的意思是：
#       >表示字节顺序是 big-endian，也就是网络序， I 表示 4 字节无符号整数。
# 注意：后面的参数个数要和处理指令一致。

# -*- unpack 把 bytes 变成相应的数据类型：
print(struct.unpack('>IH', b'\x00\x9c@cvU'))
# (10240099, 30293)
