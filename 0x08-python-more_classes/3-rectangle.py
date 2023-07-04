#!/usr/bin/python3
# 3-rectangle.py

"""Aclass Rectangle that defines a rectangle by:
(based on 2-rectangle.py)
"""


class Rectangle:
    """A rectangle representation"""

    def __init__(self, width=0, height=0):
        """Initialization of the Rectangle
        the Args:
            width: The width of  rectangle
            height: The height of rectangle
        """
        self.height = height
        self.width = width
       

    @property
    def width(self):
        """Set the width of rectangle"""

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
        """Set the height of Rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of Rectangle"""

        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of  Rectangle"""

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of Rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ("")

        Rectangle = []
        for x in range(self.__height):
            [Rectangle.append('#') for j in range(self.__width)]
            if x != self.__height - 1:
                Rectangle.append("\n")
        return ("".join(Rectangle))
