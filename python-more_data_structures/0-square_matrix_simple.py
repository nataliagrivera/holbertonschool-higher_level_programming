#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_squared = []
    for i in matrix:
        matrix_squared.append(list(map(lambda x: x**2, i)))
    return matrix_squared
