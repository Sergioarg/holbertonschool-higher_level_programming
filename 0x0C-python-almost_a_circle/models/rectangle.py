#!/usr/bin/python3
""" Module to class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Public Method Constructor

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

    @property
    def width(self):
        """ Getter of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter of height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter of x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter of y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    """ Public Method that returns the area of the rectangle  """

    def area(self):
        """ Returns the area of the rectangle """
        return (self.__height * self.__width)

    """ Public Method that dyplay the output  """

    def display(self):
        """ Display the rectangle """
        if self.__width == 0 or self.__height == 0:
            return
        print("\n" * self.__y, end="")
        for row in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    """ Public Method return output file """

    def __str__(self):
        """ Print the message of the rectangle values """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    """ Public Method that assigns an argument to each attribute """

    def update(self, *args, **kwargs):
        """ Updates all attributes of the Rectangle object. """

        if bool(args) is True and len(args) < 5 and args is not None:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for value in kwargs.keys():
                if value in dir(self):
                    setattr(self, value, kwargs[value])

    """ Public Method Returns the dictionary representation of a Rectangle """

    def to_dictionary(self):
        """ Change to dictionary """
        dictionary = {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }
        return dictionary
