#!/usr/bin/python3
"""Square module."""

class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Starts a Square instance with a defines size.

        Args:
             size: The size of the square has to be >= 0.

        Raises:
             TypeError: if size not an int
             ValueError: if size is under zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
