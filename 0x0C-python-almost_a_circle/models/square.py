#!/usr/bin/python3
""" Module to class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Public Method Constructor """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Public Method that return messege """
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ Getter of size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter of size attribute """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Public method to updates the attributes """
        if bool(args) is True and args is not None:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for value in kwargs.keys():
                if value in dir(self):
                    setattr(self, value, kwargs[value])

    def to_dictionary(self):
        """ Assing values like dictionary """
        dictionary = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return dictionary
