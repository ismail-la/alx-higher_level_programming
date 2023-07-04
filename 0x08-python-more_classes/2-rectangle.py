#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by:
(based on 1-rectangle.py)
"""


class Rectangle:
    """a rectangle reprisentation"""

    def __init__(self, width=0, height=0):

        """Initialization of the rectangle class
        the Args:
            width: the width of the rectangle
            height: the height of the rectangle
        the Raises:
            TypeError: (if the size is not integer)
            ValueError: (if the size is less than zero)
        """
        self.height = height
        self.width = width


    @property
    def width(self):
        """set width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the height of th rectangle"""

        return self.__height

    @height.setter
    def height(self, value):


        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of rectangle"""

        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of rectangle"""

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
