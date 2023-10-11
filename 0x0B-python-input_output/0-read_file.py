#!/usr/bin/python3
"""Defines read_file function."""


def read_file(filename=""):
    """Prints contents of UTF-8 file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
