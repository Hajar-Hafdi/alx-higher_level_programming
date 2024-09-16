#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    lstdvs = []
    for ur in my_list:
        if(ur % 2) == 0:
            lstdvs.append(True)
        else:
            lstdvs.append(False)
    return lstdvs
