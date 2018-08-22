# -*- coding: utf-8 -*-


def sayHello():
    strs = "hello"
    print strs

if __name__ == "__main__":
    print 'This is main of module "hello.py"'


'''1、当单独执行该module时，比如单独执行以上hello.py： python hello.py，则输出
This is main of module "hello.py"
hello
可以理解为"if __name__=="__main__":" 这一句与c中的main()函数所表述的是一致的，即作为入口

2、当该module被其它module 引入使用时，其中的"if __name__=="__main__":"所表示的
Block不会被执行,这是因为此时module被其它module引用时，其__name__的 值将发生变化
，__name__的值将会是module的名字。比如在python shell中import hello后，查看
hello.__name__：

>>> import hello
>>> hello.__name__
'hello'
>>>

3、因此，在python中，当一个module作为整体被执行时,moduel.__name__的值将
是"__main__"；而当一个 module被其它module引用时，module.__name__将是module自己
的名字，当然一个module被其它module引用时，其 本身并不需要一个可执行的入口main了

注释： __name__ 定义主要是这个模块是需要被引用，而不是本身执行，所以不需要打印
sayHello()
'''