#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    i = 0
    for i in range(x):
        try:
            while i is not x:
                print(my_list[i], end="")
                i += 1
        except IndexError:
            None
    print()
    return i
