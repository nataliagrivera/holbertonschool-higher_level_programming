#!/usr/bin/python3
def replace_elements(my_list, replacements):
    for idx, element in replacements.items():
        if 0 <= idx < len(my_list):
            my_list[idx] = element
    return my_list
