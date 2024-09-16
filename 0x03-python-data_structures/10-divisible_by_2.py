#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    maxi_value = my_list[0]
    for ber in my_list:
        if ber > maxi_value:
            maxi_value = ber
    return maxi_value
