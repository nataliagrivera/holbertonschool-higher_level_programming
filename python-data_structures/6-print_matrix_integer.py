#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in row:
            print("{:d}".format(column), end=" ") # end=" " prints a space instead of a new line))
        print() # prints a new line

