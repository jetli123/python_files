# -*- coding: utf-8 -*-
"""
  把 print()替换为 logging 是第 3 种方式，和 assert 比，logging 不会抛
出错误，而且可以输出到文件：
"""
import logging
logging.basicConfig(level=logging.INFO)

'''
    logging 的好处，它允许你指定记录信息的级别，
有 debug， info，warning，error 等几个级别，
当我们指定 level=INFO 时，logging.debug就不起作用了。
同理，指定 level=WARNING 后，debug 和 info 就不起作用
了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后
统一控制输出哪个级别的信息。
'''
# 例子1：

def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        print bar('0')
    except Exception as e:
        logging.exception(e)

# 例子2：
def test():
    s = '1'
    n = int(s)
    logging.info('n = %d' % n)
    print 10 / n

if __name__ == '__main__':
    main()
    test()

'''logging 的另一个好处是通过简单的配置，一条语句可以同时输出到不
同的地方，比如 console 和文件。'''