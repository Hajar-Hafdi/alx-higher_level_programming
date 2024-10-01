#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    u = 0
    try:
        while u is not x:
            print(my_list[u], end='')
            u += 1
    except IndexError:
        None
    print()
    return (u)
    
