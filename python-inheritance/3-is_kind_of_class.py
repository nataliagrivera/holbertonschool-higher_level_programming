#!/usr/bin/python3
"""Defines a function that returns True if the object is an instance of a class
   that inherited (directly or indirectly) from the specified class"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance 
        of a class that inherited from
        a_class"""
    
    if isinstance(obj, a_class):
        return True
    else:
        return False
