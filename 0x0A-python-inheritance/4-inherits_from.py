#!/usr/bin/python3
"""module that defines inherits_from(obj, a_class) function"""


def inherits_from(obj, a_class):
    """chacks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj: the object.
        a_class: the class to check if obj is an instance of a class
        inherited from a_class (directly or indirectly).

    Return:
        True or False
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
