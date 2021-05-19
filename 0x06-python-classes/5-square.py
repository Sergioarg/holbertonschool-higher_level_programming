#!/usr/bin/python3

""" Create the Square class """


class Square:

    """ Init stances """
    def __init__(self, size=0):
        self.size = size

    """ Property functions """
    @property
    def size(self):
        return self.__size

    """ setter the size """
    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = int(value)

    """ Public instance method """
    def area(self):
        number = self.size
        return(number * number)

    """ Function to print square  """
    def my_print(self):

        size = self.size
        if (size <= 0):
            print("")
        else:
            for row in range(size):
                for col in range(size):
                    print("#", end="")
                print("")
