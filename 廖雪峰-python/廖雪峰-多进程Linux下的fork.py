# -*- coding:utf-8 -*-
"""Unix/Linux 操作系统提供了一个 fork()系统调用，它非常特殊。普通的
函数调用，调用一次，返回一次，但是 fork()调用一次，返回两次，因
为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
然后，分别在父进程和子进程内返回。"""
# Python 的 os 模块封装了常见的系统调用，其中就包括 fork，可以在
# Python 程序中轻松创建子进程
import os


print 'Process (%s) start...' % os.getpid()
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

# 子进程永远返回 0，而父进程返回子进程的 ID。这样做的理由是，一个
# 父进程可以 fork 出很多子进程，所以，父进程要记下每个子进程的 ID，
# 而子进程只需要调用 getppid()就可以拿到父进程的 ID。
# 有了 fork 调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，
# 常见的 Apache 服务器就是由父进程监听端口，每当有新的
# http 请求时，就 fork 出子进程来处理新的 http 请求。