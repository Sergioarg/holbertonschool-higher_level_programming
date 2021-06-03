#!/usr/bin/python3
""" Class MyInt """


class MyInt(int):

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True
