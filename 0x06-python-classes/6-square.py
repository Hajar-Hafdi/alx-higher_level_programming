#!/usr/bin/python3
"""Define a class square"""

class Square:
    """Represents a square with a specified size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Starts quare with optional size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Set current size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """retrieve size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """set position for square"""
        return self.__position

    @position.setter
    def position(self, value):
        """retrieve position of square"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all (num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square with # char"""
        if self.__size == 0;
        print("")
        return

    [print("") for ur in range(0, self.__position[1])]
    for ur in range(0, self.__size):
        [print(" ", end="") for k in range(0, self.__position[0])]
        [print("#", end="") for l in range(0, self.__size)]
        print("")
