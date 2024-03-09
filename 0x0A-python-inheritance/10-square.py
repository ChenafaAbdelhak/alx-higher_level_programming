#!/usr/bin/python3
"""module class square"""
BaseGeometry = __import__('9-rectangle').Rectangle



class Square(Rectangle):
    """square class inherits from rectangle"""

    def __init__(self, size) -> None:
        """initialize a new square"""
        self.integer__validator("size", size)
        super().__init__(size, size)
        self.__size = size
