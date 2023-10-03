#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C': # if char is not 'c' or 'C'
            new_string += char # adds char to new_string if not 'c' or 'C' 
    return new_string
