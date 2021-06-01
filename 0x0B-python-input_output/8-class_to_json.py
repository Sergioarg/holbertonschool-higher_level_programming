#!/usr/bin/python3
""" Module that returns an dictionary
    description with simple data structure.
"""


def class_to_json(obj):
    """ Function class_to_json

    Args:
        obj (dict): instance of a Class
    """
    return obj.__dict__
