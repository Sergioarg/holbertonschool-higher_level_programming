#!/usr/bin/python3
""" Module to open and write files """


def write_file(filename="", text=""):
    """ Function to write the content of the file  """

    with open(filename, mode="w", encoding="utf-8") as my_file:
        return my_file.write(text)
