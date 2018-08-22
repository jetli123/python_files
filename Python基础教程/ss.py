# -*- coding: utf-8 -*-
__metaclass__ = type

class Bird:

    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("Ahaaa, I'm hungry!")
            self.hungry = False
        else:
            print("No, thanks!")


class SongBird(Bird):

    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = 'Squawk!!!'

    def sing(self):
        print self.sound


if __name__ == '__main__':
    a = SongBird()
    print a.hungry
    a.eat()
    print a.hungry
    a.eat()
    a.sing()