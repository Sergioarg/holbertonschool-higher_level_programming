#!/usr/bin/python3
""" Module of class BaseGeometry """


class BaseGeometry:
    """ Message of raise of Exception """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
