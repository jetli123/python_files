# -*- coding: utf-8 -*-
"""
    凡是用 print()来辅助查看的地方，都可以用断言（assert）来替代：
"""
__author__ = 'JetLi'

'''
    用 print()最大的坏处是将来还得删掉它，想想程序里到处都是 print()，
运行结果也会包含很多垃圾信息。所以，我们又有第二种方法 -- 断言：
'''

def foo(a):
    b = int(a)
    # 表达式 b != 0 应该是 True 继续执行，否则抛出AssertionError
    assert b != 0, 'n is zero!'
    return 10 / b

def main():
    foo('0')

main()
'''assert 的意思是，表达式 b != 0 应该是 True，否则，根据程序运行的逻
辑，后面的代码肯定会出错。
如果断言失败，assert 语句本身就会抛出 AssertionError
'''

# 程序中如果到处充斥着 assert，和 print()相比也好不到哪去。不过，
# 启动 Python 解释器时可以用-O 参数来关闭 assert

# 关闭后，你可以把所有的 assert 语句当成 pass 来看。