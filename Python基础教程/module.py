# -*- coding: utf-8 -*-
def hello():
    print 'Hello, world!'


def test():
    hello()


'''当我们在命令行运行 hello 模块文件时， Python 解释器把一个特殊变量
__name__置为__main__，而如果在其他地方导入该 hello 模块时， if 判断
将失败，因此，这种 if 测试可以让一个模块通过命令行运行时执行一
些额外的代码，最常见的就是运行测试'''
if __name__ == '__main__':
    test()
