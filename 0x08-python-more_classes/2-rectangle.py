#!/usr/bin/python3
"""Module class Rectangle"""


class Rectangle:
    """Class Rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """ Property width """
    @property
    def width(self):
        return self.__width

    """ Setter to width """
    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            value = 0
            raise ValueError("width must be >= 0")
        self.__width = value

    """ Property height """
    @property
    def height(self):
        return self.__height

    """ Setter to height """
    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            value = 0
            raise ValueError("height must be >= 0")
        self.__height = value

    """ Function return the area of rectagle """
    def area(self):
        return (self.__width * self.__height)

    """ Function return the perimeter of rectagle """
    def perimeter(self):
        return (2 * (self.__width + self.__height))
