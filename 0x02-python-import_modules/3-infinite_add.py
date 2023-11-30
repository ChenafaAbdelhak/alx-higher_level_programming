#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0
    length = len(argv)
    i = 1
    if length == 1:
        print("0")
    else:
        while i < length:
            sum += int(argv[i])
            i += 1
        print("{}".format(sum))
