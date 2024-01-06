#!/usr/bin/python3
'''
    module defines a rectangle class
'''


class Rectangle:
    '''
        class that define a rectangle
    '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return ((self.height * 2) + (self.width * 2))

    def __str__(self):
        string = ""
        if self.height == 0 or self.width == 0:
            return string
        else:
            for h in range(self.height):
                for w in range(self.width):
                    string += "#"
                string += "\n"
        return string[:-1]

    def __repr__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)
