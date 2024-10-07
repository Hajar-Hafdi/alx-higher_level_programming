#!/usr/bin/python3

"""
defines rectangle
"""

class Rectangle:
    """depicts a rectangle"""
    def __init__(self, width=0, height=0):
        """starts Rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """sets private instance attribute width"""
        return self.__width
    @width.setter
    def width(self):
        """set private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """set the private instance attribute height"""
        return self.__height
    @height.setter
    def height(self, value)
    """set private instance attribute height"""
    if type(value) is not int:
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self.__height = value
