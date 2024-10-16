#!/usr/bin/python3
"""Outlines file-writing function"""


def write_file(filename="", text=""):
    """Outputs a str to a UTF8 text file

    Args:
        filename : name of the file to write
        text : text to write to the file
    Returns:
        num of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
