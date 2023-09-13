#!/usr/bin/python3


def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for int in my_list:
        if int not in new_list:
            sum += int
            new_list.append(int)
    return sum
