#!/usr/bin/python3
'''module to add integers'''


def add_integer(a, b=98):
    """
    add two integer a + b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
   
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
