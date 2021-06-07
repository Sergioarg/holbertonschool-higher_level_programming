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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


# -----------------------------------------------------------------------------
    """ Getter and setters  """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
# -----------------------------------------------------------------------------

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

# -----------------------------------------------------------------------------
    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
# -----------------------------------------------------------------------------

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """ Public Methods """
    """ Public method that returns the area of the rectangle  """

    def area(self):
        return (self.__height * self.__width)

    """ Public Method that dyplay the output  """

    def display(self):

        if self.__width == 0 or self.__height == 0:
            return
        for row in range(self.x):
            print()
        for cols in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    """ Public Method return output file """

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    """ Public Method that assigns an argument to each attribute """

    def update(self, *args):
        num_key = 0
        key = ["id", "width", "height", "x", "y"]

        for value in args:
            if num_key < 5:
                setattr(self, key[num_key], value)
                num_key += 1
