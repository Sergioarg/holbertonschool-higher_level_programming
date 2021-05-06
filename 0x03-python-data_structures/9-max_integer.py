#!/usr/bin/python3
def max_integer(my_list=[]):
    lenght = len(my_list)

    if (lenght == 0):
        return (None)

    maxi = my_list[0]
    for item in my_list:
        if (item > maxi):
            maxi = item
    return (maxi)
