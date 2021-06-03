#!/usr/bin/python3
""" Module of class Square """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """ Function contructor that instance the private attributes

        Atrributes:
            size (int): size
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
