#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda u: replace if u == search else u, my_list))
