#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_list = []
    for n in my_list:
        if n % 2:
            div_list.append(False)
        else:
            div_list.append(True)
    return div_list
