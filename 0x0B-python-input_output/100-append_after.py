#!/usr/bin/python3
"""Outlines text file insertion function"""

def append_after(filename="", search_string="", new_string=""):
    """Embeds text after each line containing a given str

    Args:
        filename: a string depicting name of the file
        search_string: a string to search for within the file
        new_string: str to be embedded
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
