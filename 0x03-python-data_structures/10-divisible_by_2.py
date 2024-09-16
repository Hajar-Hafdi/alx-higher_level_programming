#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lstdvs = []
    for u in my_list:
        if (u % 2) == 0:
            lstdvs.append(True)
        else:
            lstdvs.append(False)
     return lstdvs
