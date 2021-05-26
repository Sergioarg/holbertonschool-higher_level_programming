#!/usr/bin/python3
"""Module to print an square """


def print_square(size):
    """ Validations of data type and loop to print the ractangle"""
    if (type(size) != int):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    elif (type(size) == float):
        raise TypeError("size must be an integer")
    else:
        for row in range(size):
            for col in range(size):
                print("#", end="")
            print("")
