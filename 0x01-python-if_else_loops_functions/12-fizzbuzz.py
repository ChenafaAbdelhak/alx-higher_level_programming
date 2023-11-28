#!/usr/bin/python3
def fuzzbuzz():
    for i in range(1, 101):
        if i % 3 != 0 and i % 5 != 0:
            print("{} ".format(i), end="")
        else:
            if i % 3 == 0:
                print("Fizz", end="")
            if i % 5 == 0:
                print("Bizz", end="")
            print(" ", end="")
