#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary): #sorted function will sort the keys in the dictionary
        print("{}: {} ".format(key,a_dictionary[key])) #.format will print the key and the value associated
