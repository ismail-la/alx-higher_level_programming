#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map((lambda r: list(map((lambda i: i * i), r))), matrix))
