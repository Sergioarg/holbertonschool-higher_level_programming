#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
msg = "Last digit of"
last = number % 10 if (number > 0) else (number % -10)

if (last == 0):
    print(msg, number, "is", last, "and is 0")
elif (last > 5):
    print(msg, number, "is", last, "and is greater than 5")
else:
    print(msg, number, "is", last, "and is less than 6 and not 0")
