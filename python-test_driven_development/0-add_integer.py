#!/usr/bin/python3
"""This module has a function that adds 2 integers"""


def add_integer(a, b=98):
    """This function adds 2 integers"""

    if a != a:
        raise ValueError("a cannot be NaN")
    if b != b:
        raise ValueError("b cannot be NaN")
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
