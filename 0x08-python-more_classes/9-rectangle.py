#!/usr/bin/python3
"""Module class Rectangle"""


class Rectangle:
    """Class Rectangle """
    """ Instance Public class attributes"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
            raise ValueError("height must be >= 0")
        self.__height = value

    """ Function return the area of rectagle """

    def area(self):
        width = self.__width
        height = self.__height
        if width == 0 or height == 0:
            return 0
        return (width * height)

    """ Function return the perimeter of rectagle """

    def perimeter(self):
        width = self.__width
        height = self.__height
        if width == 0 or height == 0:
            return 0
        return (2 * (width + height))

    """Print string"""

    def __str__(self):
        width = self.__width
        height = self.__height
        empty_char = ''

        if width == 0 or height == 0:
            return (empty_char)

        for h in range(height):
            for w in range(width):
                empty_char = empty_char + str(self.print_symbol)
            if h != height - 1:
                empty_char = empty_char + '\n'
        return empty_char

    """ Magic Method __repr__ """

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    """ Magic Method __del__ """

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    """ Static Method bigger_or_equal """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (type(rect_1) != Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif (type(rect_2) != Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1

    """ Static Method bigger_or_equal """
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
