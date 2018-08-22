# -*- coding: utf-8 -*-
"""
另一种常见的摘要算法是 SHA1，调用 SHA1 和调用 MD5 完全类似：
"""
import hashlib


sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print sha1.hexdigest()
# 2c76b57293ce30acef38d98f6046927161b46a44
# SHA1 的结果是 160 bit 字节，通常用一个 40 位的 16 进制字符串表示
