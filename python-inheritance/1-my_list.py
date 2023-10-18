#!/usr/bin/python3



class MyList(list):
    """This is a class MyList that inherits from list"""


    def print_sorted(self):
        """This function prints the list, but sorted (ascending sort)"""
        print(sorted(self))
