#!/usr/bin/python3
""" Module to decode string and json """
import json


def load_from_json_file(filename):
    """ Function that creates an Object from a “JSON file”

        Args:
            filename (str): File name used
    """
    with open(filename, encoding="utf-8") as my_file:
        return json.load(my_file)
