#!/usr/bin/python3
import sys
sys.path.append('../')
add = __import__('add_0').add
a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a, b)))
