#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y)

    # @property
    # def size(self):
    #     return self.__size
    # @size.setter
    # def size(self, value):
    #     self.width = value
    #     self.height = value

    def __str__(self):
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.__id, self.__x, self.__y, self.__size))
