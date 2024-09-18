#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    mval = 0
    mkey = None
    for ur, b in a_dictionary.items():
        if b > mval:
            mval = b
            mkey = ur
    return mkey
