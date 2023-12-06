#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_m = list(map(lambda x: replace if x == search else x, my_list))
    return list_m
