#!/usr/bin/python3
""" Module to decode string and json """
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file,
        using a JSON representation.

        Args:
            my_obj (json): Object json to write in the file
            filename (str): File name to use
    """
    with open(filename, mode="w+", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
