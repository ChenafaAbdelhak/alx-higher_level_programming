#!/usr/bin/python3
def uppercase(str):
    upper_s = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            upper_s += chr(ord(i) - 32)
        else:
            upper_s += i
    print("{}".format(upper_s))
