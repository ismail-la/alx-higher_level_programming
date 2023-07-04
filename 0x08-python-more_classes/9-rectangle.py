#!/usr/bin/python3

"""a class Rectangle that defines a rectangle by:
 (based on 8-rectangle.py)
 """


class Rectangle:
    """A rectangle representation
    the Attributes:
        number_of_instances: number of Rectangle instances
        print_symbol: symbol used for string representation
    """

    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialization of a Rectangle
        the Args:
            width: The width of the new rectangle
            height: The height of the new rectangle
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
        """Return the perimeter of Rectangle"""

        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area
        the Args:
            rect_1: first Rectangle
            rect_2: second Rectangle
        the Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle
                        The rectangle with the larger area
        """

        if not isinstance(rect_1, Rect):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rect):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with with width == height == size
        the Args:
            size: The width and height of the new Rectangle
        """

        return (cls(size, size))

    def __str__(self):
        """Return the printable representation of Rectangle"""

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

        Rect = "Rectangle(" + str(self.__width)
        Rect += ", " + str(self.__height) + ")"
        return Rect

    def __del__(self):
        """Print message for every deletion of a Rectangle"""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")
