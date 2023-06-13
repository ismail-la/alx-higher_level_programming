#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for colomn in row:
            print("{:d}".format(colomn), end=" " if col != row[-1] else "")
        print()
