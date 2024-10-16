#!/usr/bin/python3
"""
Outlines file-appending func
"""

def append_write(filename="", text=""):
    """Adds a str to the end of a UTF8 text file

    Args:
        filename: name of the file to add to
        text: string to append to the file
    Returns:
        num of chars added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
