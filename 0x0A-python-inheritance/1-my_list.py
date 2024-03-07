#!/usr/bin/python3
''' module defines a class Mylist inherits fr0m list'''


class MyList(list):
    """
    class that inherits fr0m the built-in list class and adds a
    method to print the list in ascending order.
    """

    def print_sorted(self):
        '''prints the list sorted'''
        sorted_list = sorted(self)
        print(sorted_list)
