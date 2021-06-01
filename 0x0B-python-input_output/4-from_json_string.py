#!/usr/bin/python3
""" Import module to decode string and json """
import json


def from_json_string(my_str):
    """ Fuction that returns strings to json """
    return json.loads(my_str)
