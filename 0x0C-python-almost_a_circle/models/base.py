#!/usr/bin/python3
""" Module to class Base """
import json
import csv
import os.path


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

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save information into a file """
        list = []
        if list_objs is not None:
            list = [items.to_dictionary() for items in list_objs]
        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == '':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            created_dicti = cls(1, 1)
        if cls.__name__ == "Square":
            created_dicti = cls(1)

        created_dicti.update(**dictionary)
        return created_dicti

    @classmethod
    def load_from_file(cls):
        """ load from file """

        list_instances = []
        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as file:
                str_json_file = cls.from_json_string(file.read())
                for item in str_json_file:
                    list_instances.append(cls.create(**item))
            return list_instances
        except Exception as error:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save information into a csv file """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    keys = ["id", "width", "height", "x", "y"]
                else:
                    keys = ["id", "size", "x", "y"]
                new_csv = csv.DictWriter(file, fieldnames=keys)
                for object in list_objs:
                    new_csv.writerow(object.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Load csv data """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r', newline='') as file:
                if cls.__name__ == "Rectangle":
                    keys = ["id", "width", "height", "x", "y"]
                else:
                    keys = ["id", "size", "x", "y"]
                dict_list = csv.DictReader(file, fieldnames=keys)
                dict_list = [dict([key, int(value)] for key,
                                  value in f.items())
                             for f in dict_list]
                return [cls.create(**argument) for argument in dict_list]
        except IOError:
            return []
