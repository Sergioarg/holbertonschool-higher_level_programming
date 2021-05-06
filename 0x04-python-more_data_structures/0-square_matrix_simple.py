#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = map(lambda row: list(map(lambda n: n ** 2, row)), matrix)
    new_list = list(new_matrix)
    return (new_list)
