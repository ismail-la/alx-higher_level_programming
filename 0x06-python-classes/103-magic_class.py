#!/usr/bin/python3
"""class MagicClass matching exactly a bytecode"""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """set up or initialize a MagicClass"""

        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return or get the area of MagicClass"""

        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return or get The circumference of MagicClass"""

        return (2 * math.pi * self.__radius)
