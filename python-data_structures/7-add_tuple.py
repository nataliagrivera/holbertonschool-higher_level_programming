#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = tuple_a + (0, 0)  # adds 0 to tuple_a
    tuple_b = tuple_b + (0, 0)  # adds 0 to tuple_b
    tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])  # adds tuple_a and tuple_b
    return tuple_c