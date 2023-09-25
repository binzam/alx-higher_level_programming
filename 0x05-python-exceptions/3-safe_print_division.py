#!/usr/bin/python3


def safe_print_division(a, b):
    quotnt = 0
    try:
        quotnt = a / b
    except (TypeError, ZeroDivisionError):
        quotnt = None
    finally:
        print("Inside result: {}".format(quotnt))
    return quotnt
