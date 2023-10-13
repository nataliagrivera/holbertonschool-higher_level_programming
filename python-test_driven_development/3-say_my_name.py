#!/usr/bin/python3
"""This module has a function that prints a square"""


def say_my_name(first_name, last_name=""):
    """This function prints My name is"<first name> <last_name>"""

    if first_name != str(first_name):
        raise TypeError('first_name must be a string')
    if last_name != str(last_name):
        raise TypeError('last_name must be a string')
    print('My name is {}{}'.format(first_name, last_name))
