#!/usr/bin/python3
"""module class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class inherits from rectangle"""

    def __init__(self, size) -> None:
        """initialize a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """define print() and str"""
        return "[Square] {}/{}".format(self.__size, self.__size)
