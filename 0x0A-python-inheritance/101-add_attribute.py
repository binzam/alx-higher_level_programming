#!/usr/bin/python3
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, atr, value):
    """Add a new attribute to an object if possible.

    Args:
        obj: The object to add an attribute to.
        atr: The name of the attribute to add to obj.
        value: The value of atr.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, atr, value)
