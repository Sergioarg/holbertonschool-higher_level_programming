#!/usr/bin/python3
def uppercase(str):

    to_upper = ''
    for upper in str:
        if (ord(upper) >= 97 and ord(upper) <= 122):
            to_upper += chr(ord(upper) - 32)
        else:
            to_upper += upper
    print('{:s}'.format(to_upper))
