#!/usr/bin/python3
""" Module to validate if obj is the same type of a_class """


def is_same_class(obj, a_class):
    """ Function that validate if the obj is the same type """

    if type(obj) == a_class:
        return True
    else:
        return False
