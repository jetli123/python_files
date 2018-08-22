# -*- coding: utf-8 -*-
"""
如果一个类的构造方法被重写，那么就需要调用超类（你所继承的类）的构造方法，
否则对象可能不会被正确地初始化。
"""
# SongBird 类如果要使用 Bird 类中的 hungry 特性，SongBird 类 构造新的方法必须
# 调用 其超类 Bird 的构造方法来确保进行基本的初始化。
# 两种方法能初始化 超类的方法：
""" -*- 1.调用超类构造方法的未绑定版本:"""
#  该方法在调用一个实例的方法时，该方法的self 参数会被自动绑定到实例上（这称为绑定方法）。
#  但是，如果直接调用类的方法（比如 Bird.__init__）,那么久没有实例会被绑定。
#  这要就可以自由地提供需要的 self 参数。这样的方法称为 --》 未绑定方法。
#  通过将当前的实例作为self 参数提供给未绑定方法，SongBird 就能够使用其超类构造方法的所有实现，
#  也就是属性 hungry 能被设置。
#  class SongBird(Bird):
#       def __init__(self):
#           Bird.__init__(self)
#           self.sound = 'Squawk!'
""" -*- 2.使用 super 函数, 尽量多用 super 去初始化超类"""
#  使用 super 函数，只能在新式类中使用
#  新式类定义 ： 在类的前面 添加代码 __metaclass__ = type
#  用法：当前类（SongBird 类）和对象可以作为 super 函数的参数使用，
#        调用函数返回的对象的任何方法都是调用超类的方法，而不是当前类的方法，
#        那么就可以不用SongBird 的构造方法中使用 Bird，而是直接使用 super(SongBird, self)。
#        除此之外，__init__ 方法能以一个普通的（绑定）方法被调用。
#  class SongBird(Bird):
#       def __init__(self):
#           super(SongBird, self).__init__()
#           self.sound = 'Squawk!'
# 例子：
__metaclass__ = type  # 新式类


class Bird:  # Bird 类是： SongBird的超类

    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("Aaaah......")
            self.hungry = False
        else:
            print("NO, thanks!")


class SongBird(Bird):  # SongBird 类是： Bird 类的子类

    def __init__(self):
        # 1.调用超类构造方法的未绑定版本：
        # SongBird 类中只添加了一行代码 -- Bird.__init__(self)
        # Bird.__init__(self)
        super(SongBird, self).__init__()  # 使用了 super 函数初始化超类的方法，可以调用超类的特性 hungry 了
        self.sound = 'Squawk!'

    def sing(self):
        print self.sound

if __name__ == '__main__':
    a = Bird()
    a.eat()
    a.eat()

    b = SongBird()
    b.sing()
    b.eat()
    b.eat()

