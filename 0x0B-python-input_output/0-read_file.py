#!/usr/bin/python3
"""Def file-reading function"""


def read_file(filename=""):
    """Outputs the contents of a UTF8 text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
