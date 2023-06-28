#!/usr/bin/python3
""" class Square that defines a square by: (based on task 4 file)
Define a class Square.
"""



class Square:
    """Represent a class square"""
    def __init__(self, size):
        """Initialization new square.
        """
        self.size = size

    @property
    def size(self):
        """Get and set or retrieve the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """Print square with #"""
        
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
