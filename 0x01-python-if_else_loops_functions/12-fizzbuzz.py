#!/usr/bin/python3
def fizzbuzz():

    for number in range(1, 101): # for (number = 1; number < 101; number++)
        if (number % 3 == 0 and number % 5 == 0):
            print("FizzBuzz", end=" ")
        elif (number % 3 == 0):
            print("Fizz", end=" ")
        elif (number % 5 == 0):
            print("Buzz", end=" ")
        else:
            print('{:d}'.format(number), end=" ")
