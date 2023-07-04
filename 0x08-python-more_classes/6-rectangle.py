#!/usr/bin/python3
# 6-rectangle.py

"""a class Rectangle that defines a rectangle by:
(based on 5-rectangle.py)
"""


class Rectangle:
    """A rectangle representation.
    number_of_instances: The number of Rectangle instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialization of Rectangle
        the Args:
            width : The width of rectangle
            height: The height of rectangle
        """

        type(self).number_of_instances += 1
        self.height = height
        self.width = width
        

    @property
    def width(self):
        """Set the width of Rectangle"""

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
        """Returns the perimeter ofRectangle"""

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return printable representation of Rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ("")

        Rectangle = []
        for x in range(self.__height):
            [Rectangle.append('#') for j in range(self.__width)]
            if x != self.__height - 1:
                Rectangle.append("\n")
        return ("".join(Rectangle))

    def __repr__(self):
        """Return the string representation of Rectangle"""

        Rectangle = "Rectangle(" + str(self.__width)
        Rectangle += ", " + str(self.__height) + ")"
        return Rectangle

    def __del__(self):
        """Prints message for every deletion of Rectangle"""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
