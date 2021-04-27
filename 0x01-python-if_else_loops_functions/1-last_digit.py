#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
p_last = (number % 10)
n_last = (number % -10)
msg = "Last digit of"
# POSITIVE NUMBERS
if (number > 0):
    if (p_last == 0):
        print(msg, number, "is", p_last, "and is 0")
    elif (p_last > 5):
        print(msg, number, "is", p_last, "and is greater than 5")
    else:
        print(msg, number, "is", p_last, "and is less than 6 and not 0")
# NEGATIVE NUMBERS
if (number < 0):
    if (n_last > 5):
        print(msg, number, "is", n_last, "and is greater than 5")
    else:
        print(msg, number, "is", n_last, "and is less than 6 and not 0")
