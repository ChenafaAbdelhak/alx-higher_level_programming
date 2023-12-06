#!/usr/bin/python3
def best_score(a_dictionary):

    key = None
    max_v = 0
    if not a_dictionary:
        return None
    for k, v in a_dictionary.items():
        if v > max_v:
            max_v = v
            key = k
    return key
