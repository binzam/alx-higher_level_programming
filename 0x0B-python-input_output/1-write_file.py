#!/usr/bin/python3
"""Defines write_file function."""


def write_file(filename="", text=""):
    """writes a string to UTF-8 text file filename."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
