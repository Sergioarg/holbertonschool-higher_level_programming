#!/usr/bin/python3

""" Module square """


class Square:
    """ Class square """

    __size = 0
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        """ def stances """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Property to size """
        return (self.__size)

    @property
    def position(self):
        """ Property to position """
        return (self.__position)

    @size.setter
    def size(self, value):
        """ setter the size """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """ setter of position """
        msg = "position must be a tuple of 2 positive integers"

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(msg)
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError(msg)
        elif (value[0] < 0 or value[1] < 0):
            raise TypeError(msg)
        self.__position = value

    def area(self):
        """ Public instance method """
        number = self.size
        return(number * number)

    def my_print(self):
        """ Function to print square """
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
