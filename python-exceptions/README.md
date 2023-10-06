![GIF](https://media.giphy.com/media/oYQ9HRm5Mo7VXeMNVR/giphy.gif)


# Python Exceptions Exercises

This directory contains Python exercises related to exception handling.

## Exercise 0: Safe List Printing

Write a function `safe_print_list` that prints `x` elements of a list. The function should handle exceptions using `try` and `except` statements.

**Prototype**: `def safe_print_list(my_list=[], x=0)`

- `my_list` can contain any type (integer, string, etc.).
- All elements must be printed on the same line followed by a new line.
- `x` represents the number of elements to print.
- `x` can be bigger than the length of `my_list`.
- Returns the real number of elements printed.

You are not allowed to use `len()` or import any module.

Example usage:

```python
my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list(my_list, 2)

## Exercise 1: Safe Printing of an Integers List

Write a function safe_print_integer that prints an integer using "{:d}".format(). The function should handle exceptions using try and except statements.

Prototype: def safe_print_integer(value)

value can be any type (integer, string, etc.).
The integer should be printed followed by a new line.
Returns True if value has been correctly printed (it means the value is an integer), otherwise, returns False.
You are not allowed to use type() or import any module.

Example usage:

value = 89
has_been_print = safe_print_integer(value)

## Exercise 2: Print and Count Integers
Write a function safe_print_list_integers that prints the first x elements of a list, but only if they are integers. The function should handle exceptions using try and except statements.

Prototype: def safe_print_list_integers(my_list=[], x=0)

my_list can contain any type (integer, string, etc.).
All integers have to be printed on the same line followed by a new line, other types of values must be skipped (silently).
x represents the number of elements to access in my_list.
x can be bigger than the length of my_list.
You have to use "{:d}".format() to print an integer and avoid using len() or importing any module.

Example usage:

value = 89
has_been_print = safe_print_integer(value)

## Exercise 3: Integers Division with Debug

Write a function safe_print_division that divides two integers and prints the result. The function should handle exceptions using try, except, and finally statements.

Prototype def safe_print_division(a, b)

You can assume that a and b are integers.
The result of the division should be printed in the finally: section preceded by "Inside result:".
Returns the value of the division; if an exception occurs, returns None.
You have to use "{:}".format() to print the result and avoid importing any module.

Example usage:

a = 12
b = 2
result = safe_print_division(a, b)

## Exercise 4: Divide a List

Write a function list_division that divides element by element two lists. The function should handle exceptions using try, except, and finally statements.

Prototype: def list_division(my_list_1, my_list_2, list_length)

my_list_1 and my_list_2 can contain any type (integer, string, etc.).
list_length can be bigger than the length of both lists.
Returns a new list (length = list_length) with all divisions.
If two elements can't be divided, the division result should be equal to 0.
If an element is not an integer or float, print "wrong type".
If the division can't be done (/0), print "division by 0".
If my_list_1 or my_list_2 is too short, print "out of range".
You are not allowed to import any module.

Example usage:

my_list_1 = [10, 8, 4]
my_list_2 = [2, 4, 4]
result = list_division(my_list_1, my_list_2, max(len(my_list_1), len(my_list_2)))

## Exercise 5: Raise Exception
Write a function raise_exception that raises a type exception. The function should not import any module.

Prototype: def raise_exception()

Example usage:

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

## Exercise 6: Raise a Message
Write a function raise_exception_msg that raises a name exception with a message. The function should not import any module.

Prototype: def raise_exception_msg(message="")

Example usage:

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
