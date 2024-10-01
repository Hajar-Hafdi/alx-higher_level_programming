#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for ur in range(list_length):
        try:
            new_list.append(my_list_1[ur] / my_list_2[ur])
        except ZeroDivisionError:
            new_list.append(0)
            print('divided by Zero')
            continue
        except IndexError:
            new_list.append(0)
            print('not in range')
            continue
        except TypeError:
            new_list.append(0)
            print('incorrect type')
            continue
        finally:
            pass
    return (new_list)

