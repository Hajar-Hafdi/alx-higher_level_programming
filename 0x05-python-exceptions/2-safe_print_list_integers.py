#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    o, v = 0, 0
    while o < x:
        try:
            print("{:d}".format(my_list[o]), end="")
            v += 1
        except (ValueError, TypeError):
            pass
        o += 1
    print()
    return (v)
