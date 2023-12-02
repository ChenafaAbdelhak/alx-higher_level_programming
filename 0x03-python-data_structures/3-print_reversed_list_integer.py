#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return
    for i in range(-1, (length + 1) * -1, -1):
        print("{}".format(my_list[i]))
