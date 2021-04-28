#!/usr/bin/python3
number = 0
while number < 89:
    number += 1
    if number % 10 == 0:
        number += (number // 10) + 1
    print('{:0>2d}'.format(number), end=', ' if number < 89 else '\n')
