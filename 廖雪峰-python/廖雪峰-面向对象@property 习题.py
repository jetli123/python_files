# -*- coding: utf-8 -*-
__author__ = 'JetLi'


class Screen(object):

    def __init__(self):
        self.__width = None
        self.__height = None
#        self.__resolution = None

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def resolution(self):
        return self.__width * self.__height

s = Screen()
s.width = input('Enter a width integer: ')
s.height = input('Enter a height: ')
print s.resolution
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
