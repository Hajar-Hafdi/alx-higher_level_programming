#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for ur in sorted(a_dictionary.keys()):
        print("{}: {}".format(ur, a_dictionary[ur]))
