#!/usr/bin/python3
"""defines a function that check if an object is an instance of a class that
inherited from"""


def is_kind_of_clas(obj, a_class):
    """check if an object is an instance inherited from the class

    Args:
        obj: an object.
        a_class: the class to match the type of object to.

    Return:
        True - if obj is an instance or inherited instance of a_class.
        False - otherwise
    """

    if (isinstance(obj, a_class)):
        return True
    return False
