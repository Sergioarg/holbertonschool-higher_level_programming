#!/usr/bin/python3

""" Create the Square class """


class Square:

    """ Init stances """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """ Property to size """
    @property
    def size(self):
        return (self.__size)

    """ Property to position """
    @property
    def position(self):
        return (self.__position)

    """ setter the size """
    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = int(value)

    """ setter of position """
    @position.setter
    def position(self, value):
        msg = "position must be a tuple of 2 positive integers"

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(msg)
        elif not(isinstance(value[0], int) or isinstance(value[1], int)):
            raise TypeError(msg)
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError(msg)
        self.position = value

    """ Public instance method """
    def area(self):
        number = self.size
        return(number * number)

    """ Function to print square """
    def my_print(self):

        position = self.position
        size = self.size

        if (size <= 0):
            print("")
        else:
            for col in range(position[1]):
                print()
            for i in range(size):
                for col in range(position[0]):
                    print(" ", end="")
                for row in range(size):
                    print("#", end="")
                print("")
