#!/usr/bin/python3
""" Module to Student  """


class Student:
    """ Inicialized a values of class Student

    Args:
        first_name (str): first name of the student
        last_name (str): last name of the student
        age (int): age of the student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # """ Returns the dictionary description """

    def to_json(self, attrs=None):
        # If the list comes empty, the dictionary returns all attributes

        if (attrs is None):
            return self.__dict__

        all_attrs = {}
        # Each attribute
        # attrs: firts_name, last_name, age
        for element in attrs:
            # First refers to the Self object
            # hasattr -> Valid if the element is in the object
            if hasattr(self, element):
                # getattr -> Take the value of the Tour attribute
                all_attrs[element] = getattr(self, element)
        return all_attrs
