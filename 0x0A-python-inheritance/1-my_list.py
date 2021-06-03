#!/usr/bin/python3
""" Module that class MyList of super class <List> """


class MyList(list):
    """ class MyList that inherits from list

        Arg:
        self (list): list inherits of super class list.
    """
    def print_sorted(self):

        print(sorted(self))
