#!/usr/bin/python3

""" Create the Square class """


class Square:

    """ Valid that the size is number."""

    def __init__(self, size=0):
        if(type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = int(size)

    """ Get the area of the square."""
    def area(self):
        number = self.__size
        return(number * number)
