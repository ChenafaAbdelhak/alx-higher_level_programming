#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    i = 0
    lenth = len(argv) - 1
    if lenth == 0:
        print("0 argument.")
    if lenth >= 1:
        print("{} argument".format(lenth), end="")
        if lenth == 1:
            print(":")
        else:
            print("s:")
        while i < lenth:
            print("{}: {}".format(i + 1, argv[i + 1]))
            i += 1
