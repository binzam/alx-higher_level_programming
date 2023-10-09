#!/usr/bin/python3
"""Module for MyList class"""


class MyList(list):
    """a subclass of list"""

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Method for printing sorted list."""
        print(sorted(self))
