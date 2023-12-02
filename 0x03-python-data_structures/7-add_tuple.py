#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tu = (tval(tuple_a, 0) + tval(tuple_b, 0),
          tval(tuple_b, 1) + tval(tuple_a, 1))
    return tu


def tval(tupl, i):
    if i < 0 or i >= len(tupl) or not tupl:
        return 0
    else:
        return tupl[i]
