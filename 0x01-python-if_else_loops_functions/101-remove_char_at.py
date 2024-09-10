#!/usr/bin/python3
def remove_char_at(str, n):
    newstring = ""
    for u, k in enumerate(str):
        if u != n:
            newstring += k
    return newstring
