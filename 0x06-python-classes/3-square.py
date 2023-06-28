#!/usr/bin/python3
""" class Square that defines a square by based on task 2 file"""


class Square:
    """Representation of a square."""

    def __init__(self, size=0):
        """Initialize new square class
        size: size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return square of size"""
        return (self.__size ** 2)
