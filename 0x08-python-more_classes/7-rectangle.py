#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by:
(based on 6-rectangle.py)
 """


class Rectangle:
    """A rectangle representation
        number_of_instances: number of Rectangle instances
        print_symbol : symbol used for string representation
    """
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialization a Rectangle
        the Args:
            width: The width of  rectangle
            height: The height of rectangle
        """

        type(self).number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def width(self):
        """Set the width of  Rectangle"""

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
        """Return the perimeter of Rectangle"""

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return bprintable representation of Rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ("")

        Rect = []
        for i in range(self.__height):
            [Rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                Rect.append("\n")
        return ("".join(Rect))

    def __repr__(self):
        """Return the string representation of Rectangle"""

        Rectangle = "Rectangle(" + str(self.__width)
        Rectangle += ", " + str(self.__height) + ")"
        return Rectangle

    def __del__(self):
        """Print message for every deletion of Rectangle"""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
