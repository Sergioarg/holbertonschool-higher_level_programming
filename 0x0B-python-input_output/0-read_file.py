#!/usr/bin/python3
""" Module to open and read files """


def read_file(filename=""):
    """ Function to read the content of the file  """

    with open(filename, mode="r", encoding="utf-8") as my_file:
        print(my_file.read(), end="")
