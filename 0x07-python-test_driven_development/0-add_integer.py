#!/usr/bin/python3
"""
Mod for add_integer
"""

def add_integer(a, b=98):
    """Ads two ints
    Args:
        a: 1st int
        b: 2nd int
    Raises:
        TypeError: if a, b are not integer, float

    Return:
        Returns the addition of 2 ints
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (Int, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
