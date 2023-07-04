#!/usr/bin/python3
""" class Rectangle that defines a rectangle by:
 (based on 8-rectangle.py)
 """


class Rectangle:
    """rectangle representation"""

    print_symbol = '#'
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialization a new Rectangle
        theArgs:
            width: width of the new rectangle. Default is 0
            height : height of the new rectangle. Default is 0
        """

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get width of Rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set  width of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of Rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set height of  Rectangle"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""

        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of  Rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of Rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = []
        for x in range(self.__height):
            rectangle.append(str(self.print_symbol) * self.__width)
            if x != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        """Return string representation of Rectangle"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print  message when an instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        """Return the bigger rectangle based on the area
        the Args:
            rect_1 : first rectangle
            rect_2 : second rectangle
        Returns:
            Rectangle:  rectangle with the larger area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(Rectangle, size=0):

        """Return a new Rectangle instance with width == height == size
        the Args:
            size : width and height of the square. Default is 0
        Returns:
            Rectangle: new Rectangle instance representing a square
        """
        return Rectangle(size, size)
