#!/usr/bin/python3
"""Module for print message """


def say_my_name(first_name, last_name=""):
    """Validation of strings to print"""
    if (type(first_name) != str):
        raise TypeError("first_name must be a string")
    elif (type(last_name) != str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
