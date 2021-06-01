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

    """ Returns the dictionary description """
    def to_json(self):
        return self.__dict__
