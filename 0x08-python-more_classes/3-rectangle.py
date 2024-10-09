#!/usr/bin/python3
"""
defines class Rectangle
"""

class Rectangle:
    """depiction of rectangle"""
    def __init__(self, width=0, height=0):
        """starts the rectangle"""
        self.height = height
        self.width = width
    @property
    def width(self):
        """retrieves private instance attribute width"""
        return self.__width
    @width.setter
    def width(self, value):
        """sets the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """retrieves of private instance attribute height"""
        return self.__height
    @height.setter
    def height(self, value):
        """getter for private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
