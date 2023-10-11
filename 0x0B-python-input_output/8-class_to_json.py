#!/usr/bin/python3
"""Defines class_to_json function."""


def class_to_json(obj):
    """Return the dictionary description of with simple data structure."""
    return obj.__dict__
