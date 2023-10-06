#!/usr/bin/python3
def simple_delete(a_dictionary, keys=""):
    if keys in a_dictionary:
        del a_dictionary[keys]
    return a_dictionary
