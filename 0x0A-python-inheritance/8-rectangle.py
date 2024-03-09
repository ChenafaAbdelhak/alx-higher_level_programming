#!/usr/bin/python3
"""defines a class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """Initialize a new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__heith = height
