# -*- coding: utf-8 -*-
"""spawn 类是pexpect 的主要接口，功能是启动和控制子应用程序"""

"""class pexpect.spawn(command, args=[], timeout=30, maxread = 2000, searchwindowsize=None,
logfile=None, cwd=None, env=None, ignore_sighup=True)"""

# 1.command 可以是系统任意的命令：

# child = pexpect.spawn('/usr/bin/ftp')  # 启动 ftp 客户端命令
# child = pexpect.spawn('/usr/bin/ssh user@example.com')  # 启动 ssh远程连接命令
# child = pexpect.spawn('ls -alrt /tmp')  # 运行 ls 显示 /tmp 目录内容命令

# 2.args=[], 当子程序需要参数时，还可以使用Python 列表来代替参数项：
# child = pexpect.spawn('/usr/bin/ftp', [])
# child = pexpect.spawn('/usr/bin/ssh',['user@example.com'])
# child = pexpect.spawn('ls', ['-alrt', '/tmp'])

# 3.timeout为等待结果的超时时间；
# 4.maxread 为 pexpect 从终端控制台一次读取的最大字节数；
# 5.searchwindowsize 为匹配缓冲区字符串的位置，默认是从开始位置匹配。

"""pexpect 不会解析 shell 命令当中的元字符，包括重定向 “>”、管道符“|”
或者通配符 “*”。
   解决技巧：可以将这个三个特殊元字符的命令，作为/bin/bash 的参数进行调用。"""
# 例子：
"""
child = pexpect.spawn('/bin/bash -c "ls -l |grep LOG > logs.txt"')
child.expect(pexpect.EOF)
"""
# 可以写成：
"""
shell_cmd = 'ls -l |grep LOG > logs.txt
child = pexpect.spawn('/bin/bash', ['-c', shell_cmd])
child.expect(pexpect.EOF)
"""

# 获取 pexpect 的输入与输出信息，一种写到日志文件，另一种输出到标准输出。
# 1.写到日志方法：
# child = pexpect.spawn('ls -lrt /tmp')
# fout = file('mylog.txt', 'w')
# child.logfile = fout

# 2.输出到标准输出的方法：
# child = pexpect.spawn('/bin/ls', ['-lrt', '/tmp'])
# child.logfile = sys.stdout

# 示例：实现远程 ssh 登录，登录成功后 查看当前目录文件清单，通过日志记录所有输入和输出
import pexpect


def test1():
    child = pexpect.spawn('scp', ['/root/install.log', 'root@127.0.0.1:/tmp/'], timeout=8)
    fout = file('/root/mylog.log', 'w')
    child.logfile = fout
    child.expect('Are you sure you want to continue connecting?')
    child.sendline('yes')
    child.expect("root@127.0.0.1's password: ")
    child.sendline('centos\n')
    child.expect(pexpect.EOF)


def test2():
    child = pexpect.spawn('ssh', ['root@127.0.0.1'])
    fout = file('/root/mylog1.txt', 'w')
    child.logfile = fout

    child.expect("root@127.0.0.1's password: ")
    child.sendline('centos\n')
    child.expect('#')
    child.sendline('ls -lrt')
    child.expect(pexpect.EOF)


if __name__ == '__main__':
    test2()


"""1. expect 方法："""
# expect 定义了一个子程序输出的匹配规则
# expect(pattern, timeout=-1, searchwindowsize=-1)
# 1.pattern 表示：字符串、pexpect.EOF(指向缓冲区尾部，无匹配项)、pexpect.TIMEOUT(匹配等待超时)、正则表达式
# 或者前面四种类型组成的列表（expect(['bar', pexpect.EOF, pexpect.TIMEOUT])）
# 当 pattern 为一个列表时，且不止一个列表元素被匹配，则返回的结果是子进程输出最先出现的那个元素，
# 或者是列表最左边的元素（最小索引ID）如：
"""
import pexpect
child = pexpect.spawn("echo 'foobar'")
print child.expect(['bar', 'foo', 'foobar'])
输出：1， 即 'foo' 被匹配
"""

# 2.timeout 指定等待匹配结果的超时时间，单位为秒。当超时被触发时，expect 将匹配到 pexpect.TIMEOUT；
# 3.searchwindowsize 为匹配缓冲区字符串的位置，默认是从开始位置匹配。

# 当pexpect.EOF、pexpect.TIMEOUT作为 expect 的列表参数时，匹配时将返回所有
# 列表中的索引ID，例如：

"""
index = p.expect(['good', 'bad', pexpect.EOF, pexpect.TIMEOUT])
if index == 0:
    do_something()
elif index == 1:
    do_something_else()
elif index == 2:
    do_something_thing()
elif index == 3:
    do_something_completely_different()
"""
# 以上代码等价于

"""
try:
    index = p.expect(['good', 'bad'])
    if index == 0:
        do_something()
    elif index == 1:
        do_something_else()
except EOF:
    do_some_other_thing()
except TIMEOUT:
    do_something_completely_different()
"""
