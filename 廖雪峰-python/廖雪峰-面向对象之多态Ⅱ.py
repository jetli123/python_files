# -*- coding: utf-8 -*-


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

"""你会发现，新增一个 Animal 的子类，不必对 run_twice()做任何修改，
实际上，任何依赖 Animal 作为参数的函数或者方法都可以不加修改地正
常运行，原因就在于多态.
多态的好处就是，当我们需要传入 Dog、 Cat、 Tortoise……时，我们只
需要接收 Animal 类型就可以了，因为 Dog、 Cat、 Tortoise……都是 Animal
类型，然后，按照 Animal 类型进行操作即可。由于 Animal 类型有 run()
方法，因此，传入的任意类型，只要是 Animal 类或者子类，就会自动调
用实际类型的 run()方法，这就是多态的意思：
对于一个变量，我们只需要知道它是 Animal 类型，无需确切地知道它的
子类型，就可以放心地调用 run()方法，而具体调用的 run()方法是作用
在 Animal、 Dog、 Cat 还是 Tortoise 对象上，由运行时该对象的确切类型
决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们
新增一种 Animal 的子类时，只要确保 run()方法编写正确，不用管原来
的代码是如何调用的。这就是著名的“开闭”原则：
对扩展开放：允许新增 Animal 子类；
对修改封闭：不需要修改依赖 Animal 类型的 run_twice()等函数。"""


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())

a = Animal()
b = Dog()
#c = Husky()

print isinstance(b, Animal)
