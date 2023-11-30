#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = 0;
    l = len(argv) - 1
    if l == 0:
        print("0 argument.")
    if l >= 1:
        print("{} argument".format(l), end="")
        if l == 1:
            print(":")
        else:
            print("s:")
        while i < l:
            print("{}: {}".format(i + 1, argv[i + 1]))
            i += 1
