#!/usr/bin/python3
"""Module to print an square """


def print_square(size):
    """ Validations of data type and loop to print the ractangle"""
    if (type(size) != int or type(size) == float):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    else:
        for row in range(size):
            for col in range(size):
                print("#", end="")
            print("")
