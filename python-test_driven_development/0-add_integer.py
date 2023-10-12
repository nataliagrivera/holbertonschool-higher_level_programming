#!/usr/bin/python3
def add_integer(a, b=98):
    """This function adds 2 integers
    >>> add_integer(5)
    103

    >>> add_integer()
    Traceback (most recent call last):
        ...
    TypeError: add_integer() missing 1 required positional argument: 'a'

    >>> add_integer(1.5)
    99

    >>> add_integer(-1.5)
    97

    >>> add_integer('a')
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

    >>> add_integer('a', 'b')
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

    >>> add_integer(5, 9)
    14

    >>> add_integer(5, 9, 6)
    Traceback (most recent call last):
        ...
    TypeError: add_integer() takes from 1 to 2
    positional arguments but 3 were given

    >>> add_integer(1e210, 2t3e)
        ...
    SyntaxError: invalid syntax

    >>> add_integer('abc', [1,2,3])
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
