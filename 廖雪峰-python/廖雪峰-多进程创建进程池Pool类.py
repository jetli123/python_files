# -*- coding: utf-8 -*-
from multiprocessing import Pool
import os
import time
import random

#   在使用Python进行系统管理时，特别是同时操作多个文件目录或者远程控制多台主机，
# 并行操作可以节约大量的时间。如果操作的对象数目不大时，还可以直接使用Process类动态的生成多个进程，
# 十几个还好，但是如果上百个甚至更多，那手动去限制进程数量就显得特别的繁琐，此时进程池就派上用场了。
#   Pool类可以提供指定数量的进程供用户调用，当有新的请求提交到Pool中时，如果池还没有满，
# 就会创建一个新的进程来执行请求。如果池满，请求就会告知先等待，直到池中有进程结束，
# 才会创建新的进程来执行这些请求。
def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task %s runs: %0.2f seconds.' % (name, (end - start)))


# 在Windows上要想使用进程模块，就必须把有关进程的代码写在当前.py文件的if __name__ == ‘__main__’ :
# 语句的下面，才能正常使用Windows下的进程模块。Unix/Linux下则不需要。
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)  # 创建拥有4个进程数量的进程池
    for i in range(1, 6):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    # 关闭进程池（pool），使其不在接受新的任务。
    p.close()
    # 对 Pool 对象调用 join()方法会等待所有子进程执行完毕，调用 join()
    # 之前必须先调用 close()，调用 close()之后就不能继续添加新的 Process了。
    p.join()  # 主进程阻塞等待子进程的退出，join方法必须在close或terminate之后使用。
    print('All subprocesses done.')