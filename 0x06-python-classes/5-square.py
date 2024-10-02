#!/usr/bin/python3
"""Square module."""

class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Starts square instance with a predefined size

        Args:
            size: size of square has to be >= zero
        """
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """Property for length of square

        Raises:
            TypeError: if size != int
            ValueError: if size < 0
        """
        return self.__size
    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value: size of square
        """
        if not isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    def area(self):
        """calcultae and return the area of sqaure

        Returns:
            The size of square
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with #"""
        for ur in range(self.size):
            for k in range(self.size):
                print("#", end="\n" if k is self.size - 1 and ur != k else "")
        print()
