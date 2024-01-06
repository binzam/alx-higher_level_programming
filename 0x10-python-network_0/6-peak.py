#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    left = 0
    right = len(list_of_integers) - 1
    int_list = list_of_integers
    while left < right:
        mid = (left + right) // 2
        if int_list[mid] > int_list[mid - 1] & int_list[mid] > int_list[mid + 1]:
            return int_list[mid]
        elif int_list[mid] < int_list[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return int_list[left]
