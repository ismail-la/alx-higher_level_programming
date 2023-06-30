#!/usr/bin/python3
"""class Square that defines a square by: (based on task 5 file)"""


class Square:
    """Representation of the square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization new square """

        self.size = size
        self.position = position

    @property
    def size(self):
        """Get and set or retrieve the size of the square"""

        return (self.__size)

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get and set or retrieve the position
        of the square
        """

        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return: the area of square"""

        return (self.__size ** 2)

    def my_print(self):
        """Print the square with #"""

        if self.__size == 0:
            print("")
            return

        [print("") for b in range(0, self.__position[1])]
        for b in range(0, self.__size):
            [print(" ", end="") for c in range(0, self.__position[0])]
            [print("#", end="") for d in range(0, self.__size)]
            print("")
