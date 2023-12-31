#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    isInt = True
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        print("Exception:", err, file=sys.stderr)
        isInt = False
        return isInt
