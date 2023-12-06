#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = dict()
    for key in list(a_dictionary):
        new_dic[key] = int(a_dictionary[key]) * 2
    return new_dic
