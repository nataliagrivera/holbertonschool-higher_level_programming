#!/usr/bin/python3
"""Module for inherits_from method"""



def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited
    (directly or indirectly) from the specified class ; otherwise False"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
    