#!/usr/bin/python3
""" Module to class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Class constructor """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class Constructor

        Args:
            width (int): Value integer of width
            height (int): Value integer of height
            x (int): Value integer of x
            y (int): Value integer of y
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    """ Functions getter and setters """

    """ Getter and setter of width """
    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    """ Getter and setter of height """
    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    """ Getter and setter of x """
    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if (type(value) != int):
            raise TypeError("x must be an integer")
        if (value <= 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    """ Getter and setter of y """
    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if (type(value) != int):
            raise TypeError("y must be an integer")
        if (value <= 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    """ Public Methods """

    def area(self):
        """ Return the area of the rectangle  """
        width = self.__width
        height = self.__height
        if width == 0 or height == 0:
            width = 0
            height = 0

        return (width * height)

    """ Function that dyplay the output  """

    def display(self):

        if self.__width == 0 or self.__height == 0:
            print('')
        else:
            for h in range(self.__height):
                for w in range(self.__width):
                    print("#", end="")
                print("")

    """ Method return output file """

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.x,
                                                                 self.y,
                                                                 self.width,
                                                                 self.height)
