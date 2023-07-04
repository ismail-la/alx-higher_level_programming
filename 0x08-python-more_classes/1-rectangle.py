#!/usr/bin/python3

"""A class Rectangle that defines a rectangle by:(based on 0-rectangle.py"""


class Rectangle:
    """a rectangle representation"""

    def __init__(self, width=0, height=0):
        """Initialisation of rectangle class
        the Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """get or set the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get or set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height attribute"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
