#!/usr/bin/python3
"""Module to add two integers"""


def add_integer(a, b=98):
    """Function to return the result of two integers
    """
    if not(type(a) == int or type(a) == float):
        raise TypeError("a must be an integer")
    elif not(type(b) == int or type(b) == float):
        raise TypeError("b must be an integer")
    return int(a + b)
