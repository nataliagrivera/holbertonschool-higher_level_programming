#!/usr/bin/python3

def print_square(size):
    """This function prints a square with the character #."""
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size)
