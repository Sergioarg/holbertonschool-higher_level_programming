#!/usr/bin/python3
def uppercase(string):

    to_upper = ''
    for upper in string:
        if (ord(upper) >= 97 and ord(upper) <= 122):
            to_upper += chr(ord(upper) - 32)
        else:
            to_upper += upper
    print(to_upper)
