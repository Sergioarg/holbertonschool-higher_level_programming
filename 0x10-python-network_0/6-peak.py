#!/usr/bin/python3
""" Module for find the peak """


def find_peak(list_of_integers):
    """ Function that fintd the peak """
    if not list_of_integers:
        return None
    else:
        list_of_integers.sort()
        return(list_of_integers[-1])
