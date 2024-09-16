#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for smatrix in matrix:
        if len(smatrix) == 0:
            print()
            for u in range(len(smatrix)):
                print("{:d}".format(smatrix[u]),
                        end="\n" if u is len(smatrix) - 1 else " ")
