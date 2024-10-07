#!/usr/bin/python3
"""
defines class rectangle
"""
class Rectangle:
    """depiction of rectangle"""
    def __init__(self, width=0, height=0):
        """starts rectangle"""
        self.width = width
        self.height = height
    @property
    def width(self):
        """sets private instance attribute width"""
        return self.__width
    @width.setter
    def width(self, value):
        """sts private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """sets private instance attribute height"""
        return self.__height
    @height.setter
    def height(self, value):
        """gets private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height
    def perimeter(self):
        """returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__width * 2) + (self.__height * 2)
