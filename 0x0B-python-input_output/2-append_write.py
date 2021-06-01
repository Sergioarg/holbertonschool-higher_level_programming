#!/usr/bin/python3
""" Module to open and append files """


def append_write(filename="", text=""):
    """ Function to append the content of the file  """

    with open(filename, mode="a+", encoding="utf-8") as my_file:
        return my_file.write(text)
