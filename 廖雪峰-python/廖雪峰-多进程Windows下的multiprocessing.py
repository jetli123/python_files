# -*- coding:utf-8 -*-
"""
multiprocessing 模块提供了一个 Process 类来代表一个进程对象，下面
的例子演示了启动一个子进程并等待其结束：
"""
from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__ == "__main__":
    print 'Parent process %s.' % os.getpid()
    # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process 实例
    p = Process(target=run_proc, args=('test',))
    print 'Child process will start.'
    p.start()  # 用 start()方法启动，这样创建进程比 fork()还要简单。
    p.join()  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print 'Child process end.'