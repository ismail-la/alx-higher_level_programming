#!/usr/bin/python3
"""Define class Square.
class Square that defines a square by: (based on task 3 file)
"""


class Square:
    """Representation of the square."""

    def __init__(self, size=0):
        """Initialize new square"""
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
        """Return: the area of the square"""
        return (self.__size ** 2)
