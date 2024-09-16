#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is None:
        return None
    lstdvs = []
    for u in my_list:
        if (u % 2) == 0:
            lstdvs.append(True)
        else:
            lstdvs.append(False)
    return lstdvs
