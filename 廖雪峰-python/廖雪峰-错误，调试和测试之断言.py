# -*- coding: utf-8 -*-
__author__ = 'JetLi'

"""第一种方法简单直接粗暴有效，就是用 print()把可能有问题的变量打印出来看看"""

"""用 print()最大的坏处是将来还得删掉它，想想程序里到处都是 print()，
运行结果也会包含很多垃圾信息。"""

"""第二种方法 断言"""

# 凡是用 print()来辅助查看的地方，都可以用断言（assert）来替代：

# 程序中如果到处充斥着 assert，和 print()相比也好不到哪去。不过，
# 启动 Python 解释器时可以用-O 参数来关闭 assert：
# 关闭后，你可以把所有的 assert 语句当成 pass 来看


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    a = 10 / n
    return a


def main():
    foo('1')


if __name__ == "__main__":
    print main()

"""把 print()替换为 logging 是第 3 种方式，和 assert 比， logging 不会抛
出错误，而且可以输出到文件："""