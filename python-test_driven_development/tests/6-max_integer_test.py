#!/usr/bin/python3
"""Unittest for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer

def max_integer(list=[]):
    """This function finds the biggest integer of a list."""
    if len(list) == 0:
        return None
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max
