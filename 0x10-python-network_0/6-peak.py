#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    left = 0
    right = len(list_of_integers) - 1
    list = list_of_integers
    while left < right:
        mid = (left + right) // 2
        if list[mid] > list[mid - 1] & list[mid] > list[mid + 1]:
            return list[mid]
        elif list[mid] < list[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return list[left]
