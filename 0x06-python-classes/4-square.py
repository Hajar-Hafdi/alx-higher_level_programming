#!/usr/bin/python3
"""Square module."""

class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Strats a Square instance with predefined size.

        Args:
            size: size of Square, it has to be >= 0
        """
        self.size = size

    @property
    def size(self):
        """Property for length of square

        Rises:
           TypeError: if size turns out not an int
           ValueError: if size is < 0
        """

    @size.setter
    def size(self, value):
        """sets the size of square

        Args:
            value: size of square

        Raises:
            TypeError: If value is not an int
            ValueError: If value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate area of the square.

        Returns:
            int: area of square.
        """
        return self.__size ** 2
