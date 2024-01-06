#!/usr/bin/python3
'''
    module defines a rectangle class
'''


class Rectangle:
    '''
        class that define a rectangle
    '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self) -> int:
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
                    string += str(self.print_symbol)
                string += "\n"
        return string[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_2 > area_1:
            return rect_2
        else:
            return rect_1
