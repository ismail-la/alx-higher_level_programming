#!/usr/bin/python3
"""class Square
class Square that defines a square by: (based on task 8file.
"""


class Square:
    """define a class square"""

    def __init__(self, size=0):
        """Initialization a new square
        """
        self.size = size

    @property
    def size(self):
        """Get and set the size of the square"""

        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""

        return (self.__size ** 2)

    def __eq__(self, other):
        """Compare operator - Define the == comparision to a Square"""

        return self.area() == other.area()

    def __ne__(self, other):
        """"Compare operator != - Define the != comparison to a Square."""

        return self.area() != other.area()

    def __lt__(self, other):
        """Compare operator < - Define the < comparison to a Square."""

        return self.area() < other.area()

    def __le__(self, other):
        """ompare operator <= - Define the <= comparison to a Square."""

        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare operator > - Define the > comparison to a Square."""

        return self.area() > other.area()

    def __ge__(self, other):
        """Compare operator >= - Define the >= compmarison to a Square."""

        return self.area() >= other.area()
