#!/usr/bin/python3
""" Class MyInt """


class MyInt(int):
    """ Class MyInt return if is == or !=  """

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
