#!/usr/bin/python3
"""
Defines a Rectangle class
"""

class Rectangle:
    """
    represent Rectangle
    """
    def __init__(self, width=0, height=0):
        """ start new Rectangle
    
        Args:
            width (int): The width of new rectangle
            height (int): The height of new rectangle
        """
        self.width = width
        self.height = height
    @property
    def width(self):
        """
        set the width of the Rectangle
        """
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
        """
        set the height of the Rectangle
        """
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
        """Return the printable representation of Rectangle
        Represents rectangle with # char
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for u in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if u != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
    def __repr__(self):
        """Return the string representation of Rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
    def __del__(self):
        """Print a message for each deletion of Rectangle"""
        print("Bye rectangle...")
