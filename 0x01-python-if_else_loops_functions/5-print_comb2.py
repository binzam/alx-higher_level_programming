#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print("0{}, ".format(i))
    elif i >= 10:
        print("{}, ".format(i))
    if i == 99:
        print("{}".format(i))
