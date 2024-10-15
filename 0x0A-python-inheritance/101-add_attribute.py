#!/usr/bin/python3
"""Establishes a function that assigns attributes to objects"""

def add_attribute(obj, att, value):
    """append a new attribute to the object when applicable
    Args:
        obj: object to add an attribute to
        att: name of the attribute to add to obj
        value: value of att(attribute)
    Raises:
        TypeError: If the attribute cannot be appended
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
