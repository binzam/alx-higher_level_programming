#!/usr/bin/python3
"""Defines a class MyInt."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """== and != operators inverted."""
        return int(self) != value

    def __ne__(self, value):
        """!= and == operators inverted."""
        return int(self) == value
