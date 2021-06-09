#!/usr/bin/python3
""" Module to class Base """
import json


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class constructor:

        Args:
            id (int): id of constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """

        list_1 = []
        filename = "{}.json".format(cls.__name__)
        if list_objs is not None:
            for i in range(len(list_objs)):
                list_1.append(cls.to_dictionary(list_objs[i]))
        with open(filename, mode="w", encoding="utf-8") as json_file:
            json_file.write(cls.to_json_string(list_1))

    @classmethod
    def from_json_string(json_string):
        if json_string is None or json_string == '':
            return []
        else:
            return json.load(json_string)



    # @classmethod
    # def create(cls, **dictionary):
